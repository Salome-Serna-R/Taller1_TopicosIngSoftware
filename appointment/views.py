from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import AppointmentForm, ReminderForm
from .models import Reminder

# Importamos los services (nuevos)
from .services.reminder_service import ReminderService
from .services.gmail_service import GmailService

import os.path
import datetime as dt
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dateutil import parser


# Function to handle appointment form
def form(request):
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            creds = None

            # Carga o solicita credenciales
            if os.path.exists("token.json"):
                creds = Credentials.from_authorized_user_file("token.json")
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        "client_secret_158471176816-dc1tg1eho7hbef8ehsu6rgpv7tucnp13.apps.googleusercontent.com.json",
                        SCOPES
                    )
                    creds = flow.run_local_server(port=0)

                with open("token.json", "w") as token_file:
                    token_file.write(creds.to_json())

            try:
                service = build("calendar", "v3", credentials=creds)
                timeDateTime = parser.isoparse(form.cleaned_data['appointment_date'])
                endtime = (timeDateTime + dt.timedelta(hours=1)).isoformat()

                event = {
                    "summary": "Mental health appointment",
                    "start": {"dateTime": form.cleaned_data['appointment_date'], "timezone": "GMT-5"},
                    "end": {"dateTime": endtime, "timezone": "GMT-5"},
                    "reminders": {
                        'useDefault': False,
                        'overrides': [
                            {'method': 'email', 'minutes': 24 * 60},
                            {'method': 'email', 'minutes': 10},
                            {'method': 'popup', 'minutes': 10}
                        ]
                    }
                }

                service.events().insert(
                    calendarId=form.cleaned_data['patient_email'],
                    body=event,
                    sendUpdates='all'
                ).execute()

            except HttpError as e:
                print(f"An error occurred: {e}")

            return redirect('success_form')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()
    return render(request, 'fill_appointment.html', {'form': form})



# Success page after form submission
def success_form(request):
    return render(request, 'success_form.html')


# Function to create a reminder
@login_required
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()

            # Aquí aplicamos la inversión de dependencias
            email_service = GmailService()
            reminder_service = ReminderService(email_service)
            reminder_service.send_reminder(reminder)

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ReminderForm()
    return render(request, 'create_reminder.html', {'form': form})


# Function to list reminders for the logged-in user
@login_required
def reminder_list(request):
    current_time = timezone.now()
    reminders = Reminder.objects.filter(
        user=request.user,
        reminder_date__gte=current_time
    )
    return render(request, 'reminder_list.html', {'reminders': reminders})


# Context processor to add future reminder count to all templates
def get_future_reminders(request):
    if request.user.is_authenticated:
        future_reminder_count = Reminder.objects.filter(
            user=request.user,
            reminder_date__gte=timezone.now()
        ).count()
    else:
        future_reminder_count = 0
    return {'future_reminder_count': future_reminder_count}


# Function to edit a reminder
@login_required
def edit_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'edit_reminder.html', {'form': form, 'reminder': reminder})


# Function to delete a reminder
@login_required
def delete_reminder(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id, user=request.user)
    if request.method == 'POST':
        reminder.delete()
        return HttpResponseRedirect(reverse('reminder_list'))
    return render(request, 'confirm_delete.html', {'reminder': reminder})

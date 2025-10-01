from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Appointment
from .forms import AppointmentForm


# --------- CBV CRUD de Appointment ---------
class AppointmentList(ListView):
    model = Appointment
    paginate_by = 20
    ordering = ["-created_at"]
    template_name = "appointment/appointment_list.html"


class AppointmentCreate(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("appointment:list")
    template_name = "appointment/appointment_form.html"


class AppointmentUpdate(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("appointment:list")
    template_name = "appointment/appointment_form.html"


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy("appointment:list")
    template_name = "appointment/appointment_confirm_delete.html"


# --------- Acciones de estado (State pattern) ---------
def appointment_confirm(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.confirm()
    messages.success(request, f"Cita #{appt.pk} confirmada.")
    return redirect("appointment:list")


def appointment_complete(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.complete()
    messages.success(request, f"Cita #{appt.pk} completada.")
    return redirect("appointment:list")


def appointment_cancel(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.cancel()
    messages.success(request, f"Cita #{appt.pk} cancelada.")
    return redirect("appointment:list")


# --- Context processor dummy para compatibilidad (antes usaba Reminder) ---
def get_future_reminders(request):
    # Ya no usamos el modelo Reminder; devolvemos 0 para que las plantillas sigan funcionando
    return {"future_reminder_count": 0}

from django import forms
from .models import Appointment, Reminder


#Form to take the appointment details
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'patient_name', 
            'patient_email', 
            'patient_phone', 
            'appointment_date',
            ]
        
class ReminderForm(forms.ModelForm):
    reminder_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'] 
    )

    class Meta:
        model = Reminder
        fields = ['reminder_date', 'reminder_title', 'reminder_message', 'reminder_email']

    def clean_reminder_email(self):
        email = self.cleaned_data.get('reminder_email')
        if not email:
            raise forms.ValidationError('Por favor, introduce un correo válido.')
        return email
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

#Model to store the appointment details
class AvailableAppointment(models.Model):
    date = models.DateTimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.date)
    
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=15)
    date_options = [
        ("2024-09-07T10:35:00-05:00", "September 7 10:35AM"),
        ("2024-09-08T10:25:00-05:00", "September 8 10:25AM"),
        ("2024-09-09T11:00:00-05:00", "September 9 11AM"),
        ("2024-09-11T09:00:00-05:00", "September 11 9AM"),
        ("2024-09-23T16:00:00-05:00", "September 23 4PM"),
        ("2024-09-30T14:30:00-05:00", "September 30 2:30PM"),

    ]

    appointment_date = models.CharField(max_length=30, choices=date_options, default="2024-09-06T13:00:00+00:00")
    
    def __str__(self):
        return self.patient_name
 
#Model to store the reminder details    
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")  
    reminder_title = models.CharField(max_length=200)
    reminder_message = models.TextField()
    reminder_date = models.DateTimeField()
    reminder_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.reminder_title
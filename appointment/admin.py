from django.contrib import admin
from .models import Appointment, AvailableAppointment


# Register your models here.

admin.site.register(Appointment)
admin.site.register(AvailableAppointment)


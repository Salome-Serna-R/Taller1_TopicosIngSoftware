from django.contrib import admin
from .models import Appointment, AvailableAppointment
from .models import Appointment, Reminder


# Register your models here.

admin.site.register(Appointment)
admin.site.register(AvailableAppointment)
admin.site.register(Reminder)


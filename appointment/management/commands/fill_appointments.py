from appointment.models import AvailableAppointment
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        AvailableAppointment.objects.create(date='2024-09-03 10:00:00')
        AvailableAppointment.objects.create(date='2024-09-14 07:40:00')
        AvailableAppointment.objects.create(date='2024-09-19 12:30:00')
        AvailableAppointment.objects.create(date='2024-09-28 13:00:00')
        AvailableAppointment.objects.create(date='2024-10-02 14:00:00')
        AvailableAppointment.objects.create(date='2024-10-13 15:00:00')
        AvailableAppointment.objects.create(date='2024-10-22 16:00:00')
        AvailableAppointment.objects.create(date='2024-10-30 09:00:00')
        """
        AvailableAppointment.objects.create(date='2024-09-7 10:30:00')
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .domain.state import (
    AppointmentContext, get_state,
    REQUESTED, CONFIRMED, COMPLETED, CANCELLED
)
from .domain.events import AppointmentCreated, AppointmentStatusChanged
from .domain.bus import bus

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

    # 👇 NUEVO campo para el patrón State
    status = models.CharField(
        max_length=16,
        choices=[
            (REQUESTED, "Requested"),
            (CONFIRMED, "Confirmed"),
            (COMPLETED, "Completed"),
            (CANCELLED, "Cancelled"),
        ],
        default=REQUESTED,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name

    # 👇 MÉTODOS del patrón State + Observer
    @classmethod
    def create(cls, **kwargs):
        appt = cls.objects.create(**kwargs)
        bus.publish(AppointmentCreated(
            appointment_id=appt.pk,
            payload={"status": appt.status},
            occurred_on=timezone.now(),
        ))
        return appt

    def _transition(self, action: str) -> None:
        ctx = AppointmentContext(status=self.status)
        state = get_state(self.status)
        old = self.status

        if action == "confirm":
            state.confirm(ctx)
        elif action == "complete":
            state.complete(ctx)
        elif action == "cancel":
            state.cancel(ctx)
        else:
            raise ValueError("Acción no soportada")

        if ctx.status != old:
            self.status = ctx.status
            self.save(update_fields=["status"])
            bus.publish(AppointmentStatusChanged(
                appointment_id=self.pk,
                old_status=old,
                new_status=self.status,
                occurred_on=timezone.now(),
            ))

    def confirm(self):
        self._transition("confirm")

    def complete(self):
        self._transition("complete")

    def cancel(self):
        self._transition("cancel")

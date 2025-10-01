from django.apps import AppConfig

class AppointmentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "appointment"

    def ready(self):
        from .domain.bus import bus
        from .domain.events import AppointmentCreated, AppointmentStatusChanged
        from . import handlers  # <-- importa el módulo handlers

        bus.subscribe(AppointmentCreated, handlers.handle_appointment_created)
        bus.subscribe(AppointmentStatusChanged, handlers.handle_appointment_status_changed)

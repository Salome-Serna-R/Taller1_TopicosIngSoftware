# appointment/handlers.py
import logging
from .domain.events import AppointmentCreated, AppointmentStatusChanged

log = logging.getLogger(__name__)

def handle_appointment_created(event: AppointmentCreated) -> None:
    log.info("[Observer] Nueva cita creada id=%s status=%s",
             event.appointment_id, event.payload.get("status"))

def handle_appointment_status_changed(event: AppointmentStatusChanged) -> None:
    log.info("[Observer] Cita id=%s cambió de %s a %s",
             event.appointment_id, event.old_status, event.new_status)

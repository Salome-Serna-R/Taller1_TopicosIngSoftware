from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict

@dataclass(frozen=True)
class DomainEvent:
    occurred_on: datetime

@dataclass(frozen=True)
class AppointmentCreated(DomainEvent):
    appointment_id: int
    payload: Dict[str, Any]

@dataclass(frozen=True)
class AppointmentStatusChanged(DomainEvent):
    appointment_id: int
    old_status: str
    new_status: str

from dataclasses import dataclass

# Estados posibles
REQUESTED = "REQUESTED"
CONFIRMED = "CONFIRMED"
COMPLETED = "COMPLETED"
CANCELLED = "CANCELLED"

class InvalidTransition(Exception):
    """Error si se intenta una transición no válida."""
    pass

@dataclass
class AppointmentContext:
    status: str

# Clase base
class State:
    name: str
    def confirm(self, ctx: AppointmentContext):
        raise InvalidTransition(f"No se puede confirmar desde {self.name}")
    def complete(self, ctx: AppointmentContext):
        raise InvalidTransition(f"No se puede completar desde {self.name}")
    def cancel(self, ctx: AppointmentContext):
        raise InvalidTransition(f"No se puede cancelar desde {self.name}")

# Estados concretos
class Requested(State):
    name = REQUESTED
    def confirm(self, ctx): ctx.status = CONFIRMED
    def cancel(self, ctx): ctx.status = CANCELLED

class Confirmed(State):
    name = CONFIRMED
    def complete(self, ctx): ctx.status = COMPLETED
    def cancel(self, ctx): ctx.status = CANCELLED

class Completed(State):
    name = COMPLETED

class Cancelled(State):
    name = CANCELLED

# Mapa para obtener el estado según el valor
STATE_MAP = {
    REQUESTED: Requested(),
    CONFIRMED: Confirmed(),
    COMPLETED: Completed(),
    CANCELLED: Cancelled(),
}

def get_state(status: str) -> State:
    return STATE_MAP[status]

from typing import Callable, DefaultDict, Type, List
from collections import defaultdict

class EventBus:
    def __init__(self) -> None:
        self._handlers: DefaultDict[type, List[Callable]] = defaultdict(list)

    def subscribe(self, event_type: Type, handler: Callable) -> None:
        """Suscribir un handler a un tipo de evento."""
        self._handlers[event_type].append(handler)

    def publish(self, event) -> None:
        """Publicar un evento a todos suscriptores registrados."""
        for handler in self._handlers.get(type(event), []):
            handler(event)

# Instancia global que puedes importar y usar en todo el proyecto
bus = EventBus()

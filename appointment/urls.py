from django.urls import path
from .views import (
    AppointmentList, AppointmentCreate, AppointmentUpdate, AppointmentDelete,
    appointment_confirm, appointment_complete, appointment_cancel
)

app_name = "appointment"

urlpatterns = [
    path("", AppointmentList.as_view(), name="list"),
    path("new/", AppointmentCreate.as_view(), name="create"),
    path("<int:pk>/edit/", AppointmentUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", AppointmentDelete.as_view(), name="delete"),
    path("<int:pk>/confirm/", appointment_confirm, name="confirm"),
    path("<int:pk>/complete/", appointment_complete, name="complete"),
    path("<int:pk>/cancel/", appointment_cancel, name="cancel"),
]

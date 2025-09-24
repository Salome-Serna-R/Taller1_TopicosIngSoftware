"""
URL configuration for WeCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from emergency import views as emergency_views
from appointment import views as appointment_views
from Account import views as Account_views
import Forum.views as Forum_views
from library import views as library_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Account_views.home, name='home'),
    path('fillAppointment/', appointment_views.form, name='fill_appointment'),
    path('appointmentFiled/', appointment_views.success_form, name='success_form'),
    path('emergency/', emergency_views.emergency, name='emergency'),
    path('reminder/', appointment_views.create_reminder, name='create_reminder'),
    path('comentarios/', Forum_views.comentarios_view, name='comentarios'),  # Lista de comentarios
    path('perfil/', Account_views.perfil_view, name='perfil'),  # Perfil del usuario (comentarios propios)
    path('comentario/<int:id>/', Forum_views.detalle_comentario, name='detalle-comentario'),  # Detalles de un comentario
    path('comentario/crear/', Forum_views.comentario_create, name='crear-comentario'),  # Crear comentario
    path('comentario/editar/<int:id>/', Forum_views.comentario_edit, name='editar-comentario'),  # Editar comentario
    path('comentario/eliminar/<int:id>/', Forum_views.comentario_delete, name='eliminar-comentario'),  # Eliminar comentario
    path('comentario/<int:comentario_id>/respuesta/crear/', Forum_views.respuesta_create, name='crear-respuesta'),  # Crear respuesta
    path('respuesta/eliminar/<int:id>/', Forum_views.respuesta_delete, name='eliminar-respuesta'),  # Eliminar respuesta
    path('buscar/', Forum_views.buscar_comentario, name='buscar-comentario'),  # Buscar comentario
    path('reminder_list/', appointment_views.reminder_list, name='reminder_list'),
    path('logout/', Account_views.logout_view, name='logout'),
    path('login/', Account_views.login_view, name='login'),
    path('register/', Account_views.register_view, name='register'),
    path('library/', library_views.mental_health_library, name='library'),
    path("statistics/", library_views.search_statistics, name='statistics'),
    path('comentario/favorito/<int:comentario_id>/', Forum_views.favorite, name='marcar-favorito'),
    path('comentario/<int:comentario_id>/like/', Forum_views.like_toggle, name='like-toggle'),
    path('reminder/edit/<int:reminder_id>/', appointment_views.edit_reminder, name='edit_reminder'),
    path('reminder/delete/<int:reminder_id>/', appointment_views.delete_reminder, name='delete_reminder'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

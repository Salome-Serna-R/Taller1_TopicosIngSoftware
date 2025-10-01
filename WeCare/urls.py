from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from emergency import views as emergency_views
from Account import views as Account_views
import Forum.views as Forum_views
from library import views as library_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home / Auth
    path("", Account_views.home, name="home"),
    path("logout/", Account_views.logout_view, name="logout"),
    path("login/", Account_views.login_view, name="login"),
    path("register/", Account_views.register_view, name="register"),

    # Emergency
    path("emergency/", emergency_views.emergency, name="emergency"),

    # Forum
    path("comentarios/", Forum_views.comentarios_view, name="comentarios"),
    path("perfil/", Account_views.perfil_view, name="perfil"),
    path("comentario/<int:id>/", Forum_views.detalle_comentario, name="detalle-comentario"),
    path("comentario/crear/", Forum_views.comentario_create, name="crear-comentario"),
    path("comentario/editar/<int:id>/", Forum_views.comentario_edit, name="editar-comentario"),
    path("comentario/eliminar/<int:id>/", Forum_views.comentario_delete, name="eliminar-comentario"),
    path("comentario/<int:comentario_id>/respuesta/crear/", Forum_views.respuesta_create, name="crear-respuesta"),
    path("respuesta/eliminar/<int:id>/", Forum_views.respuesta_delete, name="eliminar-respuesta"),
    path("buscar/", Forum_views.buscar_comentario, name="buscar-comentario"),
    path("comentario/favorito/<int:comentario_id>/", Forum_views.favorite, name="marcar-favorito"),
    path("comentario/<int:comentario_id>/like/", Forum_views.like_toggle, name="like-toggle"),

    # Library
    path("library/", library_views.mental_health_library, name="library"),
    path("statistics/", library_views.search_statistics, name="statistics"),

    # Appointments (CRUD + State) — nuevo enrutamiento
    path("appointments/", include("appointment.urls", namespace="appointment")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

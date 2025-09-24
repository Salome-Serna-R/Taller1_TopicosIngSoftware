from django.contrib import admin

# Register your models here.

from .models import Comentario, Favorito, Respuesta, Like

admin.site.register(Comentario)
admin.site.register(Respuesta)
admin.site.register(Favorito)
admin.site.register(Like)
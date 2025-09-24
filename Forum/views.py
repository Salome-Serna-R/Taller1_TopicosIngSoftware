from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.

def comentarios_view(request):
    comentarios = Comentario.objects.order_by('-fecha_creacion')
    return render(request, 'Forum/comentarios.html', {'comentarios': comentarios})

@login_required(login_url='/login/')
def like_toggle(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    like, created = Like.objects.get_or_create(usuario=request.user, comentario=comentario)
    

    if not created:
        like.delete() 

    return redirect('detalle-comentario', id=comentario_id)



def detalle_comentario(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
        respuestas = Respuesta.objects.filter(comentario_id=id)
        es_favorito = False
        tiene_like = False

        if request.user.is_authenticated:
            es_favorito = Favorito.objects.filter(usuario=request.user, comentario=comentario).exists()
            tiene_like = Like.objects.filter(usuario=request.user, comentario=comentario).exists()

        total_likes = Like.objects.filter(comentario=comentario).count()
        mensaje_verificacion = total_likes >= 3

        return render(request, 'Forum/detalle_comentarios.html', {
            'comentario': comentario, 
            'respuestas': respuestas, 
            'es_favorito': es_favorito,
            'tiene_like': tiene_like,
            'total_likes': total_likes,
            'mensaje_verificacion': mensaje_verificacion
        })
    except Comentario.DoesNotExist:
        return render(request, 'Forum/comentarios.html', {'mensaje': 'El comentario no existe'})



@login_required(login_url='/login/')
def comentario_create(request):
    if request.method == 'POST':
        texto = request.POST['texto']
        autor_id = request.user.id
        comentario = Comentario(texto=texto, autor_id=autor_id)
        comentario.save()
        return redirect('perfil')
    else:
        return render(request, 'Forum/crear_comentario.html')

@login_required(login_url='/login/')
def comentario_edit(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
        if request.user.id != comentario.autor_id:
            return render(request, 'Forum/comentarios.html', {'mensaje': 'No puedes editar este comentario'})
        
        if request.method == 'POST':
            comentario.texto = request.POST['texto']
            comentario.save()
            return redirect('detalle-comentario', id=id)
        else:
            return render(request, 'Forum/editar_comentario.html', {'comentario': comentario})
    except Comentario.DoesNotExist:
        return render(request, 'Forum/comentarios.html', {'mensaje': 'El comentario no existe'})

@login_required(login_url='/login/')
def comentario_delete(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
        if request.user.id == comentario.autor_id:
            comentario.delete()
            return redirect('perfil')
        else:
            return render(request, 'Forum/comentarios.html', {'mensaje': 'No puedes eliminar este comentario'})
    except Comentario.DoesNotExist:
        return render(request, 'Forum/comentarios.html', {'mensaje': 'El comentario no existe'})
    
@login_required(login_url='/login/')
def favorite(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, comentario=comentario)
    
    if not created:
        # Si ya existe el favorito, eliminarlo
        favorito.delete()
    
    return redirect('detalle-comentario', id=comentario_id)

@login_required(login_url='/login/')
def respuesta_create(request, comentario_id):
    if request.method == 'POST':
        texto = request.POST['texto']
        autor_id = request.user.id
        respuesta = Respuesta(texto=texto, autor_id=autor_id, comentario_id=comentario_id)
        respuesta.save()
        return redirect('detalle-comentario', id=comentario_id)
    else:
        return redirect('detalle-comentario', id=comentario_id)

@login_required(login_url='/login/')
def respuesta_delete(request, id):
    try:
        respuesta = Respuesta.objects.get(id=id)
        comentario_id = respuesta.comentario_id
        if request.user.id == respuesta.autor_id or request.user.id == Comentario.objects.get(id=comentario_id).autor_id:
            respuesta.delete()
            return redirect('detalle-comentario', id=comentario_id)
        else:
            return render(request, 'Forum/comentarios.html', {'mensaje': 'No puedes eliminar esta respuesta'})
    except Respuesta.DoesNotExist:
        return render(request, 'Forum/comentarios.html', {'mensaje': 'La respuesta no existe'})

def buscar_comentario(request):
    if request.method == 'POST':
        texto = request.POST['texto'].strip()
        
        if not texto:
            comentarios = Comentario.objects.all()
        else:
            comentarios_texto = Comentario.objects.filter(texto__icontains=texto)
            comentarios_autor = Comentario.objects.filter(autor__username__icontains=texto)
            comentarios = comentarios_texto.union(comentarios_autor)
        
        mensaje = 'No se encontraron resultados para tu búsqueda.' if not comentarios.exists() else ''
        
        return render(request, 'Forum/comentarios.html', {'comentarios': comentarios, 'mensaje': mensaje})
    else:
        return redirect('comentarios')



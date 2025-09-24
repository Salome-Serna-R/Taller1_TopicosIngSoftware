from django.shortcuts import render
from django.http import HttpResponse
from Forum.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from Account.forms import FormCrearUsuario
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def perfil_view(request):
    comentarios = Comentario.objects.filter(autor_id=request.user.id)
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('comentario')
    comentarios_favoritos = [favorito.comentario for favorito in favoritos]
    
    return render(request, 'Account/perfil.html', {
        'comentarios': comentarios,
        'comentarios_favoritos': comentarios_favoritos
    })


def login_view(request):
  if request.method == 'POST':
    usuario = request.POST['usuario']
    clave = request.POST['clave']
    user = authenticate(request, username=usuario, password=clave)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return render(request, 'Account/login.html', {'mensaje': 'Usuario o clave incorrectos'})
  else:
    if request.user.is_authenticated:
      return redirect('home')
    else:
      return render(request, 'Account/login.html')
    
def register_view(request):
  if request.method == 'POST':
    form = FormCrearUsuario(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else:
      return render(request, 'Account/register.html', {'form': form})
  else:
    form = FormCrearUsuario()
    return render(request, 'Account/register.html', {'form': form})
  
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') 
    return redirect('home') 


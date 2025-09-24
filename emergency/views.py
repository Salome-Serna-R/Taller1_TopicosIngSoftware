from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def emergency(request):
    return render(request, 'emergency.html')
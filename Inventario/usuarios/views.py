from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.

def login(request):
    return render(request, 'login.html')

def add(request):
    return render(request, 'cadastro.html')

def list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.

def login(request):
    return render(request, 'login.html')

def add(request):
    form = UsuarioForm()
    data = {'form' : form}
    return render(request, 'cadastro.html', data)

def list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

def usuario_novo(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/usuarios/login/')

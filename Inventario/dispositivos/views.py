from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dispositivo
from .forms import DispositivoForm

def add(request):
    form = DispositivoForm()
    data = {'form' : form}
    return render(request, 'cadastroDispositivo.html', data)

def list(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'menu-3d.html', {'dispositivos': dispositivos})

def dispositivo_novo(request):
    form = DispositivoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/dispositivos/')

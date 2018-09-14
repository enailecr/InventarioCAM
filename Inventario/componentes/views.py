from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Componente
from .forms import ComponenteForm

def componente_novo(request):
    form = Componente(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/componentes/')

def add(request):
    form = ComponenteForm()
    data = {'form' : form}
    return render(request, 'cadastroComponente.html', data)

def list(request):
    componentes = Componente.objects.all()
    return render(request, 'menu-2c.html', {'componentes': componentes})

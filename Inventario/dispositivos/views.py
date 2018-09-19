from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dispositivo
from .forms import DispositivoForm
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    form = DispositivoForm()
    data = {'form' : form}
    return render(request, 'cadastroDispositivo.html', data)

@login_required
def list(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'menu-3d.html', {'dispositivos': dispositivos})

@login_required
def dispositivo_novo(request):
    form = DispositivoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/dispositivos/')

@login_required
def dispositivo_edita(request, id):
    data = {}
    dispositivo = Dispositivo.objects.get(id=id)
    form = DispositivoForm(request.POST or None, instance=dispositivo)
    data['dispositivo'] = dispositivo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/dispositivos/')
    else:
        return render(request, 'editaDispositivo.html', data)

@login_required
def dispositivo_remove(request, id):
    dispositivo = Dispositivo.objects.get(id=id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('/dispositivos/')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dispositivo
from .forms import DispositivoForm
from django.contrib.auth.decorators import login_required
import re
from django_tables2 import RequestConfig
from .tables import DispositivoTable

@login_required
def add(request):
    form = DispositivoForm()
    data = {'form' : form}
    return render(request, 'cadastroDispositivo.html', data)

@login_required
def list(request):
    table = DispositivoTable(Dispositivo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'menu-3d.html', {'table': table})

@login_required
def dispositivo_busca(request):
    dispositivos = Dispositivo.objects.all()
    filter = request.GET.get('search')
    if filter:
        disp = []
        for dispositivo in dispositivos:
            if re.search(filter, dispositivo.unidade.sigla, re.IGNORECASE):
                disp.append(dispositivo)
        dispositivos = disp
    table = DispositivoTable(dispositivos)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'menu-3d.html', {'table': table})

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
    dispositivo.delete()
    return redirect('/dispositivos/')

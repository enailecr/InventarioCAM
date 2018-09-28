from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Componente
from .forms import ComponenteForm
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from .tables import ComponenteTable
import re

@login_required
def componente_novo(request):
    form = ComponenteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/componentes/')

@login_required
def add(request):
    form = ComponenteForm()
    data = {'form' : form}
    return render(request, 'cadastroComponente.html', data)

@login_required
def list(request):
    table = ComponenteTable(Componente.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'menu-2c.html', {'table': table})

@login_required
def componente_busca(request):
    componentes = Componente.objects.all()
    filter = request.GET.get('search')
    if filter:
        comp = []
        for componente in componentes:
            if (re.search(filter, componente.sigla, re.IGNORECASE) or re.search(filter, componente.nome, re.IGNORECASE)):
                comp.append(componente)
        componentes = comp
    table = ComponenteTable(componentes)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'menu-2c.html', {'table': table})

@login_required
def componente_edita(request, id):
    data = {}
    componente = Componente.objects.get(id=id)
    form = ComponenteForm(request.POST or None, instance=componente)
    data['componente'] = componente
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/componentes/')
    else:
        return render(request, 'editaComponente.html', data)

@login_required
def componente_remove(request, id):
    componente = Componente.objects.get(id=id)
    componente.delete()
    return redirect('/componentes/')

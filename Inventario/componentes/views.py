from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Componente
from .forms import ComponenteForm
from django.contrib.auth.decorators import login_required

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
    componentes = Componente.objects.all()
    return render(request, 'menu-2c.html', {'componentes': componentes})

@login_required
def componente_busca(request):
    componentes = Componente.objects.all()
    filter = request.GET.get('search')
    print(filter)
    if filter:
        componentes = componentes.filter(nome__icontains=filter)
    return render(request, 'menu-2c.html', {'componentes': componentes})

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

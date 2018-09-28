from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required
import re
from django_tables2 import RequestConfig
from .tables import ContatoTable

@login_required
def add(request):
    form = ContatoForm()
    data = {'form' : form}
    return render(request, 'cadastroContato.html', data)

@login_required
def list(request):
    table = ContatoTable(Contato.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'menu-contatos.html', {'table': table})

@login_required
def contato_busca(request):
    contatos = Contato.objects.all()
    filter = request.GET.get('search')
    if filter:
        cont = []
        for contato in contatos:
            if (re.search(filter, contato.email, re.IGNORECASE) or re.search(filter, contato.nome, re.IGNORECASE)):
                cont.append(contato)
        contatos = cont
    table = ContatoTable(contatos)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'menu-contatos.html', {'table': table})

@login_required
def contato_novo(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/contatos/')

@login_required
def contato_edita(request, id):
    data = {}
    contato = Contato.objects.get(id=id)
    form = ContatoForm(request.POST or None, instance=contato)
    data['contato'] = contato
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/contatos/')
    else:
        return render(request, 'editaContato.html', data)

@login_required
def contato_remove(request, id):
    contato = Contato.objects.get(id=id)
    contato.delete()
    return redirect('/contatos/')

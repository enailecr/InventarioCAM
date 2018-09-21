from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    form = ContatoForm()
    data = {'form' : form}
    return render(request, 'cadastroContato.html', data)

@login_required
def list(request):
    contatos = Contato.objects.all()
    return render(request, 'menu-contatos.html', {'contatos': contatos})

@login_required
def contato_busca(request):
    contatos = Contato.objects.all()
    filter = request.GET.get('search')
    if filter:
        contatos = contatos.filter(nome__icontains=filter)
    return render(request, 'menu-contatos.html', {'contatos': contatos})

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

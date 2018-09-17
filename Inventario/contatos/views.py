from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato
from .forms import ContatoForm

def add(request):
    form = ContatoForm()
    data = {'form' : form}
    return render(request, 'cadastroContato.html', data)

def list(request):
    contatos = Contato.objects.all()
    return render(request, 'lista.html', {'contatos': contatos})

def contato_novo(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/contatos/')

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
        return render(request, 'editaContatos.html')

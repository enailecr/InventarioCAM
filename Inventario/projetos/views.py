from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projeto
from .forms import ProjetoForm
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    form = ProjetoForm()
    data = {'form' : form}
    return render(request, 'cadastroProjeto.html', data)

@login_required
def list(request):
    projetos = Projeto.objects.all()
    return render(request, 'menu-1p.html', {'projetos': projetos})

@login_required
def projeto_novo(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/projetos/')

@login_required
def projeto_edita(request, id):
    data = {}
    projeto = Projeto.objects.get(id=id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    data['projeto'] = projeto
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/projetos/')
    else:
        return render(request, 'editaProjeto.html', data)

@login_required
def projeto_remove(request, id):
    projeto = Projeto.objects.get(id=id)
    projeto.delete()
    return redirect('/projetos/')

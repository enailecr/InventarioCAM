from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projeto
from .forms import ProjetoForm

def add(request):
    form = ProjetoForm()
    data = {'form' : form}
    return render(request, 'cadastroProjeto.html', data)

def list(request):
    projetos = Projeto.objects.all()
    return render(request, 'menu-1p.html', {'projetos': projetos})

def projeto_novo(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/projetos/')

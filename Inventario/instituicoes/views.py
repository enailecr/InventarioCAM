from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Instituicao, Unidade
from .forms import InstituicaoForm, UnidadeForm

def add_inst(request):
    form = InstituicaoForm()
    data = {'form' : form}
    return render(request, 'cadastroInstituicao.html', data)

def add_unid(request):
    form = UnidadeForm()
    data = {'form' : form}
    return render(request, 'cadastroUnidade.html', data)

def list_inst(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'menu-3d.html', {'instituicoes': instituicoes})

def list_unid(request):
    unidades = Unidade.objects.all()
    return render(request, 'menu-5u.html', {'unidades': unidades})

def instituicao_novo(request):
    form = InstituicaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/instituicoes/')

def unidade_novo(request):
    form = UnidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/instituicoes/unidades/')

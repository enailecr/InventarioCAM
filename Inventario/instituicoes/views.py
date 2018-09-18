from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Instituicao, Unidade
from .forms import InstituicaoForm, UnidadeForm
from django.contrib.auth.decorators import login_required

@login_required
def add_inst(request):
    form = InstituicaoForm()
    data = {'form' : form}
    return render(request, 'cadastroInstituicao.html', data)

@login_required
def add_unid(request):
    form = UnidadeForm()
    data = {'form' : form}
    return render(request, 'cadastroUnidade.html', data)

@login_required
def list_inst(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'menu-4i.html', {'instituicoes': instituicoes})

@login_required
def list_unid(request):
    unidades = Unidade.objects.all()
    return render(request, 'menu-5u.html', {'unidades': unidades})

@login_required
def instituicao_novo(request):
    form = InstituicaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/instituicoes/')

@login_required
def unidade_novo(request):
    form = UnidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/instituicoes/unidades/')

@login_required
def instituicao_edita(request):
    data = {}
    instituicao = Instituicao.objects.get(id=id)
    form = InstituicaoForm(request.POST or None, instance=instituicao)
    data['instituicao'] = instituicao
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect ('/instituicoes/')
    else:
        return render(request, 'editaInstituicao.html')

@login_required
def unidade_edita(request):
    data = {}
    unidade = Unidade.objects.get(id=id)
    form = UnidadeForm(request.POST or None, instance=unidade)
    data['unidade'] = unidade
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect ('/instituicoes/unidades/')
    else:
        return render(request, 'editaUnidade.html')

@login_required
def instituicao_remove(request, id):
    instituicao = Instituicao.objects.get(id=id)
    if request.method == 'POST':
        instituicao.delete()
        return redirect('/instituicoes/')

@login_required
def unidade_remove(request, id):
    unidade = Unidade.objects.get(id=id)
    if request.method == 'POST':
        unidade.delete()
        return redirect('/instituicoes/unidades/')

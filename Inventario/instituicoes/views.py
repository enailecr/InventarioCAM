from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Instituicao, Unidade
from .forms import InstituicaoForm, UnidadeForm
from django.contrib.auth.decorators import login_required
from dispositivos.models import Anotacao
from dispositivos.forms import AnotacaoForm
import re

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
def instituicao_busca(request):
    instituicoes = Instituicao.objects.all()
    filter = request.GET.get('search')
    if filter:
        inst = []
        for instituicao in instituicoes:
            if (re.search(filter, instituicao.nome, re.IGNORECASE) or re.search(filter, instituicao.sigla, re.IGNORECASE)):
                inst.append(instituicao)
        instituicoes = inst
    return render(request, 'menu-4i.html', {'instituicoes': instituicoes})

@login_required
def unidade_busca(request):
    unidades = Unidade.objects.all()
    filter = request.GET.get('search')
    if filter:
        unid = []
        for unidade in unidades:
            if (re.search(filter, unidade.nome, re.IGNORECASE) or re.search(filter, unidade.sigla, re.IGNORECASE)):
                unid.append(unidade)
        unidades = unid
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
def instituicao_edita(request, id):
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
        return render(request, 'editaInstituicao.html', data)

@login_required
def unidade_edita(request,id):
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
        return render(request, 'editaUnidade.html', data)

@login_required
def instituicao_remove(request, id):
    instituicao = Instituicao.objects.get(id=id)
    instituicao.delete()
    return redirect('/instituicoes/')

@login_required
def unidade_remove(request, id):
    unidade = Unidade.objects.get(id=id)
    unidade.delete()
    return redirect('/instituicoes/unidades/')

@login_required
def nota_novo(request, idUnidade):
    form = AnotacaoForm(request.POST or None)
    unidade = Unidade.objects.get(id=idUnidade)
    if form.is_valid():
        post = form.save(commit=False)
        post.criadoPor = request.user
        post.unidade = unidade
        post.removido = False
        post.save()
    return redirect ('/instituicoes/unidades/notas/'+idUnidade)

@login_required
def add_nota(request, idUnidade):
    form = AnotacaoForm()
    data = {'form' : form, 'idUnidade': idUnidade}
    return render(request, 'cadastroNota.html', data)

@login_required
def nota_edita(request, id):
    data = {}
    nota = Anotacao.objects.get(id=id)
    form = AnotacaoForm(request.POST or None, instance=nota)
    data['nota'] = nota
    data['form'] = form
    idUnidade = nota.unidade.id
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.editadoPor = request.user
            post.save()
        return redirect ('/instituicoes/unidades/notas/'+ str(idUnidade))
    else:
        return render(request, 'editaNota.html', data)

@login_required
def nota_remove(request, id):
    nota = Anotacao.objects.get(id=id)
    nota.removido=True
    nota.save()
    idUnidade = nota.unidade.id
    return redirect('/instituicoes/unidades/notas/'+ str(idUnidade))

@login_required
def list_notas(request, idUnidade):
    todasNotas = Anotacao.objects.all()
    unidade = Unidade.objects.get(id=idUnidade)
    notas = []
    for nota in todasNotas:
        if unidade == nota.unidade:
            notas.append(nota)
    data = {'notas': notas, 'idUnidade' : idUnidade}
    return render(request, 'menu-6n.html',data)

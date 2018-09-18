from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

def login(request):
    return render(request, 'login.html')

def add(request):
    form = UsuarioForm()
    data = {'form' : form}
    return render(request, 'cadastro.html', data)

def list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

@require_POST
def usuario_novo(request):
    nome = request.POST['nome']
    email = request.POST['email']
    senha = request.POST['senha']
    usuario = request.POST['usuario']

    novoUsuario = User.objects.create_user(username=usuario, email=email, password=senha)
    novoUsuario.first_name = nome
    novoUsuario.save()
    return redirect ('/contas/login/')

def usuario_edita(request, id):
    data = {}
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    data['usuario'] = usuario
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/usuarios/') #mudar
    else:
        return render(request, 'editaPerfil.html')

from django.shortcuts import render

# Create your views here.

def componente_novo(request):
    form = Componente(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('componentes')

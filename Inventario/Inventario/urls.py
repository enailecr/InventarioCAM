from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path(r'', home),
    path(r'componentes/', include('componentes.urls')),
    path(r'contatos/', include('contatos.urls')),
    path(r'dispositivos/', include('dispositivos.urls')),
    path(r'instituicoes/', include('instituicoes.urls')),
    path(r'projetos/', include('projetos.urls')),
    path(r'usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]

from django.urls import path
from django.conf.urls import include, url
from .views import  add, componente_novo, list, componente_edita, componente_remove, componente_busca

urlpatterns = [
    path(r'add/',add),
    path(r'', list),
    url(r'componente-novo/',componente_novo, name='componente_novo'),
    url(r'componente-edita/(?P<id>\d+)/$', componente_edita, name='componente_edita'),
    url(r'componente-remove/(?P<id>\d+)/$', componente_remove, name='componente_remove'),
    url(r'componente-busca/', componente_busca, name='componente_busca'),
]

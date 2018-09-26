from django.urls import path
from django.conf.urls import include, url
from .views import list_inst, list_unid, add_inst, add_unid, instituicao_novo, unidade_novo, unidade_edita, instituicao_edita, instituicao_remove, unidade_remove, nota_novo, add_nota, nota_edita, nota_remove, list_notas, unidade_busca, instituicao_busca

urlpatterns = [
    path(r'', list_inst),
    url(r'add/',add_inst),
    url(r'add-uni/',add_unid),
    url(r'unidades/unidade-novo/', unidade_novo, name='unidade_novo'),
    url(r'instituicao-novo/', instituicao_novo, name='instituicao_novo'),
    url(r'instituicao-edita/(?P<id>\d+)/$', instituicao_edita, name='instituicao_edita'),
    url(r'unidades/unidade-edita/(?P<id>\d+)/$', unidade_edita, name='unidade_edita'),
    url(r'instituicao-remove/(?P<id>\d+)/$', instituicao_remove, name='instituicao_remove'),
    url(r'instituicao-busca/', instituicao_busca, name='instituicao_busca'),
    url(r'unidades/unidade-remove/(?P<id>\d+)/$', unidade_remove, name='unidade_remove'),
    url(r'unidades/unidade-busca/', unidade_busca, name='unidade_busca'),
    url(r'unidades/notas/(?P<idUnidade>\d+)/$', list_notas, name='notas'),
    url(r'add-nota/(?P<idUnidade>\d+)/$', add_nota, name='add_nota'),
    url(r'unidades/nota-novo/', nota_novo, name='nota_novo'),
    url(r'unidades/nota-edita/(?P<id>\d+)/$', nota_edita, name='nota_edita'),
    url(r'unidades/nota-remove/(?P<id>\d+)/$', nota_remove, name='nota_remove'),
    path(r'unidades/', list_unid),
]

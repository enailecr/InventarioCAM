from django.urls import path
from django.conf.urls import include, url
from .views import list_inst, list_unid, add_inst, add_unid, instituicao_novo, unidade_novo, unidade_edita, instituicao_edita

urlpatterns = [
    path(r'', list_inst),
    path(r'unidades/', list_unid),
    path(r'add-inst/',add_inst),
    path(r'add-unid/',add_unid),
    url(r'instituicao-novo/', instituicao_novo, name='instituicao_novo'),
    url(r'unidade-novo/', unidade_novo, name='unidade_novo'),
    url(r'instituicao-edita/(?P<id>\d+)/$', instituicao_edita, name='instituicao_edita'),
    url(r'unidade-edita/(?P<id>\d+)/$', unidade_edita, name='unidade_edita'),
]

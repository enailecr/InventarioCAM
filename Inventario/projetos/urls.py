from django.urls import path
from django.conf.urls import include, url
from .views import list, add, projeto_novo, projeto_remove, projeto_edita

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'projeto-novo/',projeto_novo, name='projeto_novo'),
    url(r'projeto-edita/(?P<id>\d+)/$', projeto_edita, name='projeto_edita'),
    url(r'projeto-remove/(?P<id>\d+)/$', projeto_remove, name='projeto_remove'),
]

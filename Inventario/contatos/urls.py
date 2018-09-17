from django.urls import path
from django.conf.urls import include, url
from .views import list, add, contato_novo, contato_edita, contato_remove

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'contato-novo/',contato_novo, name='contato_novo'),
    url(r'contato-edita/(?P<id>\d+)/$', contato_edita, name='contato_edita'),
    url(r'contato-remove/(?P<id>\d+)/$', contato_remove, name='contato_remove'),
]

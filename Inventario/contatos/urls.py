from django.urls import path
from django.conf.urls import include, url
from .views import list, add, contato_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'contato-novo/',contato_novo, name='contato_novo'),
]

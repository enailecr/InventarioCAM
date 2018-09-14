from django.urls import path
from django.conf.urls import include, url
from .views import  add, componente_novo, list

urlpatterns = [
    path(r'add/',add),
    path(r'', list),
    url(r'componente-novo/',componente_novo, name='componente_novo'),
]

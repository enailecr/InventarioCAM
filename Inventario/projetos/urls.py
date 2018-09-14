from django.urls import path
from django.conf.urls import include, url
from .views import list, add, projeto_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'projeto-novo/',projeto_novo, name='projeto_novo'),
]

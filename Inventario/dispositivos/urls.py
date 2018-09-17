from django.urls import path
from django.conf.urls import include, url
from .views import list, add, dispositivo_novo

urlpatterns = [
    path(r'', list, name='list'),
    path(r'add/',add),
    url(r'dispositivo-novo/',dispositivo_novo, name='dispositivo_novo'),
]

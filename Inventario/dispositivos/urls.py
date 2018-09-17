from django.urls import path
from django.conf.urls import include, url
from .views import list, add, dispositivo_novo, dispositivo_edita

urlpatterns = [
    path(r'', list, name='list'),
    path(r'add/',add),
    url(r'dispositivo-novo/',dispositivo_novo, name='dispositivo_novo'),
    url(r'dispositivo-edita/(?P<id>\d+)/$', dispositivo_edita, name='dispositivo_edita'),
]

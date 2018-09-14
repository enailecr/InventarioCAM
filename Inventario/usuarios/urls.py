from django.urls import path
from django.conf.urls import include, url
from .views import login, add, usuario_novo

urlpatterns = [
    path(r'login/', login),
    path(r'add/',add),
    url(r'usuario-novo/',usuario_novo, name='usuario_novo'),
    # path('accounts/', include('django.contrib.auth.urls')),
]

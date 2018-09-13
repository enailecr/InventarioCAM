from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import login, add

urlpatterns = [
    path(r'login/', login),
    path(r'add/',add),
    path('accounts/', include('django.contrib.auth.urls')),
]

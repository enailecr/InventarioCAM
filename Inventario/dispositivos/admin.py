from django.contrib import admin
from .models import StatusDispositivos, Anotacao, Dispositivo

admin.site.register(StatusDispositivos)
admin.site.register(Dispositivo)
admin.site.register(Anotacao)

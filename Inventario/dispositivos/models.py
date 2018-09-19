from django.db import models
from projetos.models import Projeto
from componentes.models import Componente
from instituicoes.models import Unidade

# Create your models here.

class Dispositivo(models.Model):
    ip = models.CharField(max_length=25, blank=True, null=True)
    ipvirtual = models.CharField(max_length=25, blank=False, null=False)
    status = models.ForeignKey('StatusDispositivos', on_delete=models.CASCADE,)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE,)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE,)

    def __str__(self):
        return self.ip

class StatusDispositivos(models.Model):
    status = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.status

class Anotacao(models.Model):
    nota = models.CharField(max_length=255, blank=False, null=False)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE, blank=True, null=True)

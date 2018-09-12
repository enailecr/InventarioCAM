from django.db import models
from projetos.models import Projeto
from componentes.models import Componente
from instituicoes.models import Unidade

# Create your models here.

class Dispositivo(models.Model):
    ip = models.CharField(max_length=25, blank=True, null=True)
    ipvirtual = models.CharField(max_length=25, blank=False, null=False)
    fkstatus = models.ForeignKey('StatusDispositivos', on_delete=models.CASCADE,)
    fkprojeto = models.ForeignKey(Projeto, on_delete=models.CASCADE,)
    fkcomponente = models.ForeignKey(Componente, on_delete=models.CASCADE,)
    fkunidade = models.ForeignKey(Unidade, on_delete=models.CASCADE,)

class StatusDispositivos(models.Model):
    status = models.CharField(max_length=45, blank=False, null=False)

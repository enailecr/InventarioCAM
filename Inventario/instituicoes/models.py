from django.db import models
from contatos.models import Contato

# Create your models here.

class Instituicao(models.Model):
    sigla = models.CharField(max_length=35, blank=False, null=False)
    nome = models.CharField(max_length=255, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    idEstatistica = models.CharField(max_length=45, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    num = models.CharField(max_length=7, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=55, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    contatos = models.ManyToManyField(Contato, blank=True)

    def __str__(self):
        return self.nome

class Unidade(models.Model):
    sigla = models.CharField(max_length=35, blank=False, null=False)
    nome = models.CharField(max_length=255, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    servidor = models.CharField(max_length=20, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    num = models.CharField(max_length=7, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=55, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    posicaogeo = models.CharField(max_length=85, blank=True, null=True)
    fkinstituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE,)
    contatos = models.ManyToManyField(Contato, blank=True)

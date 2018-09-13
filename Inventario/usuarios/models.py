from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField()
    usuario = models.CharField(max_length=16, blank=False, null=False)
    senha = models.CharField(max_length=255, blank=False, null=False)
    nome = models.CharField(max_length=200, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    fkpermissao = models.ForeignKey('Permissao', on_delete=models.CASCADE,)

    def __str__(self):
        return self.nome

class Permissao(models.Model):
    tipo = models.CharField(max_length=45, blank=False, null=False)

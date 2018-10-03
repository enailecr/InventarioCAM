from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    sigla = models.CharField(max_length=35, blank=False, null=False)
    editar = "teste"
    # Editar = <input type="text">
    excluir = "tata"
    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.

class Componente(models.Model):
    sigla = models.CharField(max_length=35, blank=False, null=False)
    nome = models.CharField(max_length=255, blank=False, null=False)
    versao = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.ForeignKey('TipoComponente', on_delete=models.CASCADE,)
    editar = "teste"
    # Editar = <input type="text">
    excluir = "tata"
    
    def __str__(self):
        return self.nome

class TipoComponente(models.Model):
    tipo = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.tipo

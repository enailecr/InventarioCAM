from django.db import models

# Create your models here.

class Contato(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=200, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

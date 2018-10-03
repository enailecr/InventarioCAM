from django.db import models
from contatos.models import Contato

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'))

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
    estado = models.CharField(max_length=2, blank=True, null=True, choices=ESTADOS)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    contatos = models.ManyToManyField(Contato, blank=True)
    editar = "teste"
    # Editar = <input type="text">
    excluir = "tata"

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
    estado = models.CharField(max_length=2, blank=True, null=True, choices=ESTADOS)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    latitude = models.CharField(max_length=85, blank=True, null=True)
    longitude = models.CharField(max_length=85, blank=True, null=True)
    instituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE,)
    contatos = models.ManyToManyField(Contato, blank=True)
    editar = "teste"
    # Editar = <input type="text">
    excluir = "tata"
    nota = "botao nota"

    def __str__(self):
        return self.nome

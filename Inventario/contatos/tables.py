import django_tables2 as tables
from .models import Contato

class ContatoTable(tables.Table):
    class Meta:
        model = Contato
        fields = ('nome', 'email', 'telefone')

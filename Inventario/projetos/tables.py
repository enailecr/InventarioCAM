import django_tables2 as tables
from .models import Projeto

class ProjetoTable(tables.Table):
    class Meta:
        model = Projeto
        fields = ('sigla', 'nome')

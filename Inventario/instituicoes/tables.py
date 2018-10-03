import django_tables2 as tables
from .models import Instituicao, Unidade

class InstituicaoTable(tables.Table):
    class Meta:
        model = Instituicao
        fields = ('sigla', 'nome','editar','excluir')

class UnidadeTable(tables.Table):
    class Meta:
        model = Unidade
        fields = ('instituicao', 'sigla', 'nome','editar','nota','excluir')

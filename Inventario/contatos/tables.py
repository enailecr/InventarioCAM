import django_tables2 as tables
import django_filters
from .models import Contato

class ContatoTable(tables.Table):
    class Meta:
        model = Contato
        fields = ('nome', 'email', 'telefone','editar','excluir')

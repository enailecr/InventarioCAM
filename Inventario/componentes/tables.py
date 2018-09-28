import django_tables2 as tables
from .models import Componente

class ComponenteTable(tables.Table):
    class Meta:
        model = Componente
        fields = ('sigla', 'tipo', 'nome', 'versao')

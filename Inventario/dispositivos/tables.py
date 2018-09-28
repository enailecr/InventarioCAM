import django_tables2 as tables
from .models import Dispositivo

class DispositivoTable(tables.Table):
    class Meta:
        model = Dispositivo
        fields = ('unidade.instituicao.sigla', 'unidade.sigla', 'projeto', 'componente', 'ip', 'core', 'web', 'ipvirtual', 'atualizado', 'status')
        labels = {
            'ipvirtual': ('Extra'),
        }

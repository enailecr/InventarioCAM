import django_tables2 as tables
from .models import Dispositivo

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class DispositivoTable(tables.Table):
    excluir = tables.TemplateColumn(
            '<form action="/dispositivos/dispositivo-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
        orderable=False,
        verbose_name=''
        )
    editar = tables.TemplateColumn(
            '<form action="/dispositivos/dispositivo-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        fields = ('unidade.instituicao.sigla', 'unidade.sigla', 'projeto', 'componente', 'ip', 'core', 'web', 'ipvirtual', 'atualizado', 'status','editar','excluir')
        atualizado  = tables.BooleanColumn('atualizado')
        model = Dispositivo
        template_name = 'django_tables2/bootstrap.html'
        labels = {
            'ipvirtual': ('Extra'),
        }

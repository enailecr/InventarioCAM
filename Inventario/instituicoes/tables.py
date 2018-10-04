import django_tables2 as tables
from .models import Instituicao, Unidade

class InstituicaoTable(tables.Table):
    excluir = tables.TemplateColumn(
            '<form action="/instituicoes/instituicao-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
        orderable=False,
        verbose_name=''
        )
    editar = tables.TemplateColumn(
            '<form action="/instituicoes/instituicao-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        model = Instituicao
        fields = ('sigla', 'nome','editar','excluir')

class UnidadeTable(tables.Table):
    excluir = tables.TemplateColumn(
            '<form action="/instituicoes/unidades/unidade-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
        orderable=False,
        verbose_name=''
        )
    editar = tables.TemplateColumn(
            '<form action="/instituicoes/unidades/unidade-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
        orderable=False,
        verbose_name=''
        )
    nota = tables.TemplateColumn(
            '<form action="/instituicoes/unidades/notas/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Notas</button></form>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        model = Unidade
        fields = ('instituicao', 'sigla', 'nome','editar','nota','excluir')

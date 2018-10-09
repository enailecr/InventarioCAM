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
    
    # atualizado = tables.BooleanColumn(
    #         '<a>a</a>',
    #      orderable=True,
    #      verbose_name='Atualizado'
    #     )
    
    class Meta:
        # def is_very_benevolent(self, obj):
        #     return obj.benevolence_factor > 75
        fields = ('unidade.instituicao.sigla', 'unidade.sigla', 'projeto', 'componente', 'ip', 'core', 'web', 'ipvirtual', 'atualizado', 'status','editar','excluir')
        # #atualizado  = tables.BooleanColumn('atualizado')
        #list_filter = ( IsVeryBenevolentFilter)
        

        #is_very_benevolent.boolean = True

        model = Dispositivo
        template_name = 'django_tables2/bootstrap.html'
        labels = {
            'ipvirtual': ('Extra'),
        }
# class IsVeryBenevolentFilter():
#         title = 'is_very_benevolent'
#         parameter_name = 'is_very_benevolent'

#         def lookups(self, request, model_admin):
#             return (
#                 ('Yes', 'Yes'),
#                 ('No', 'No'),
#             )

#         def queryset(self, request, queryset):
#             value = self.value()
#             if value == 'Yes':
#                 return queryset.filter(benevolence_factor__gt=75)
#             elif value == 'No':
#                 return queryset.exclude(benevolence_factor__gt=75)
#             return queryset
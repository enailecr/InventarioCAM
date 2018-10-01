import django_tables2 as tables
from .models import Projeto
from django.utils.html import format_html

class ButtonColumn(tables.Column):
    def render(self):
        return format_html('<input type="button" class="edit-button">')

class ProjetoTable(tables.Table):
    class Meta:
        model = Projeto
        editar = ButtonColumn()
        fields = ('sigla', 'nome', 'editar', 'excluir')

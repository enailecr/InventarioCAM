from django.forms import ModelForm
from .models import Unidade, Instituicao

class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

class UnidadeForm(ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'

from django.forms import ModelForm
from .models import Unidade, Instituicao
from dispositivos.models import Anotacao

class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

class UnidadeForm(ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'

class AnotacaoForm(ModelForm):
    class Meta:
        model = Anotacao
        fields = ['nota','dispositivo']

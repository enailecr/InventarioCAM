from django.forms import ModelForm
from .models import Dispositivo, Anotacao

class DispositivoForm(ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('ip', 'ipvirtual', 'status', 'projeto', 'componente', 'unidade')
        labels = {
            'ipvirtual': ('IP Virtual'),
        }

class AnotacaoForm(ModelForm):
    class Meta:
        model = Anotacao
        fields = '__all__'
        labels = {
            'ipvirtual': ('IP Virtual'),
        }

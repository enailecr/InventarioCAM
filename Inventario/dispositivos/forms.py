from django.forms import ModelForm
from .models import Dispositivo

class DispositivoForm(ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('ip', 'ipvirtual', 'status', 'projeto', 'componente', 'unidade')
        labels = {
            'ipvirtual': ('IP Virtual'),
        }

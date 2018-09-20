from django.forms import ModelForm
from .models import Componente

class ComponenteForm(ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'
        labels = {
            'versao': ('Versão'),
        }

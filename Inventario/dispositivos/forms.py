from django.forms import ModelForm
from .models import Dispositivo

class DispositivoForm(ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'

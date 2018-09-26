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

    def __init__(self, *args, **kwargs):
       self.request = kwargs.pop('request', None)
       return super(AnotacaoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
       kwargs['commit']=False
       obj = super(AnotacaoForm, self).save(*args, **kwargs)
       if self.request:
           if obj.criadoPor is null:
               obj.criadoPor = self.request.user
           else:
               obj.editadoPor = self.request.user
       obj.save()
       return obj

    class Meta:
        model = Anotacao
        fields = '__all__'

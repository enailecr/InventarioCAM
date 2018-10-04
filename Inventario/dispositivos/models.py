from django.db import models
from projetos.models import Projeto
from componentes.models import Componente
from instituicoes.models import Unidade

# Create your models here.

class Dispositivo(models.Model):
    ip = models.CharField(max_length=25, blank=False, null=False)
    ipvirtual = models.CharField(max_length=25, blank=True, null=True)
    status = models.ForeignKey('StatusDispositivos', on_delete=models.CASCADE,)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE,)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE,)
    core = models.CharField(max_length=25, blank=True, null=True)
    web = models.CharField(max_length=25, blank=True, null=True)
    atualizado = models.CharField(max_length=1, blank=True, null=True)
    #editar = models.ForeignKey('EditarDispositivo', on_delete=models.CASCADE,)
 
    #editar = "tes"
    #editar = models.type('EditarDispositivo', on_delete=models.CASCADE,)

    #editar = <input type="text">
    #excluir = "tata"
    
    def __str__(self):
        return self.ip;

    # def ativo(self):
    #     if self.atualizado == "1":
    #        return "Ativo";
    #     else:
    #         return "Inativo";

class StatusDispositivos(models.Model):
    status = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return self.status;

# class atualizadoDispositivos(models.Model):
#     atualizado = models.CharField(max_length=45, blank=False, null=False)

#     def __str__(self):
#         if self.atualizado == "1":
#            return "Ativo";
#         else:
#             return "Inativo";


# class EditarDispositivo(models.Model):
#     editar = models.CharField(max_length=45, blank=False, null=False)

#     def __str__(self):
#         return "<a href=\"#\">Teste</a>";
#         #if self.status == 1:
        #    return "Ativo" + str(self.status);
        #else:
        #    return "Inativo" + str(self.status);
              
            
class Anotacao(models.Model):
    nota = models.TextField( blank=False, null=False)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE, blank=True, null=True)
    removido = models.BooleanField(default=False)
    criadoEm = models.DateTimeField(auto_now_add=True)
    editadoEm = models.DateTimeField(auto_now=True)
    criadoPor = models.ForeignKey('auth.User', related_name='criadoPor', on_delete=models.PROTECT, editable=False, null=True)
    editadoPor = models.ForeignKey('auth.User', related_name='editadoPor', on_delete=models.PROTECT, editable=False, null=True)

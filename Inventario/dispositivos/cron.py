from dispositivos.models import Dispositivo
import os, platform

#class MyCronJob(CronJobBase):
def MyCronJob():
    ##os.system("echo blablabla >> /tmp/teste");
    dispositivos = Dispositivo.objects.all()
    if  platform.system().lower()=="windows":
        ping_str = "-n 1"
    else:
        ping_str = "-c 1"
    for dispositivo in dispositivos:
        ping = os.system("/bin/ping -c 1 " + dispositivo.ip)
        if ping == 0:
            dispositivo.atualizado = 0
            dispositivo.save()
        else:
            dispositivo.atualizado = 1
            dispositivo.save()

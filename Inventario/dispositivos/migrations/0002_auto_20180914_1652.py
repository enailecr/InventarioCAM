# Generated by Django 2.1.1 on 2018-09-14 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivo',
            old_name='fkcomponente',
            new_name='componente',
        ),
        migrations.RenameField(
            model_name='dispositivo',
            old_name='fkprojeto',
            new_name='projeto',
        ),
        migrations.RenameField(
            model_name='dispositivo',
            old_name='fkstatus',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='dispositivo',
            old_name='fkunidade',
            new_name='unidade',
        ),
    ]
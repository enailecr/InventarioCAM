# Generated by Django 2.1.1 on 2018-09-11 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('componentes', '0001_initial'),
        ('instituicoes', '0001_initial'),
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=25, null=True)),
                ('ipvirtual', models.CharField(max_length=25)),
                ('fkcomponente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='componentes.Componente')),
                ('fkprojeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='StatusDispositivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='fkstatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.StatusDispositivos'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='fkunidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituicoes.Unidade'),
        ),
    ]

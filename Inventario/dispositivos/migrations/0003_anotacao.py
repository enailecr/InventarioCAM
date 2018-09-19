# Generated by Django 2.0.5 on 2018-09-19 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituicoes', '0003_auto_20180914_1652'),
        ('dispositivos', '0002_auto_20180914_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=255)),
                ('dispositivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dispositivos.Dispositivo')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituicoes.Unidade')),
            ],
        ),
    ]

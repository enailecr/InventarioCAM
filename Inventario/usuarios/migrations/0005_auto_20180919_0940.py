# Generated by Django 2.0.5 on 2018-09-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20180914_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='permissao',
        ),
        migrations.DeleteModel(
            name='Permissao',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]

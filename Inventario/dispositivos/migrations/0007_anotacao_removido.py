# Generated by Django 2.1.1 on 2018-09-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0006_auto_20180926_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotacao',
            name='removido',
            field=models.BooleanField(default=False),
        ),
    ]

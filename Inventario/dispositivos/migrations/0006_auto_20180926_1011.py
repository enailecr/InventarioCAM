# Generated by Django 2.1.1 on 2018-09-26 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dispositivos', '0005_auto_20180925_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotacao',
            name='criadoEm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anotacao',
            name='criadoPor',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='criadoPor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anotacao',
            name='editadoEm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='anotacao',
            name='editadoPor',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='editadoPor', to=settings.AUTH_USER_MODEL),
        ),
    ]

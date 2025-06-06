# Generated by Django 5.2.1 on 2025-05-25 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_movimientoinventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoinventario',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('cancelado', 'Cancelado')], default='activo', max_length=20),
        ),
        migrations.AddField(
            model_name='movimientoinventario',
            name='sucursal_destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traspasos_destino', to='accounts.sucursal'),
        ),
    ]

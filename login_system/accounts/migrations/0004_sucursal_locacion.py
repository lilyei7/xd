# Generated by Django 5.2.1 on 2025-05-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_sucursal_capacidad_comensales_sucursal_ciudad_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='locacion',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]

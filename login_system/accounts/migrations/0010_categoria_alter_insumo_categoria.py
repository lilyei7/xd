# Generated by Django 5.2.1 on 2025-05-20 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_insumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('icono', models.CharField(default='fa-cube', max_length=50)),
                ('color_fondo', models.CharField(default='#f3f4f6', max_length=20)),
                ('color_icono', models.CharField(default='#374151', max_length=20)),
                ('activa', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterField(
            model_name='insumo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='insumos', to='accounts.categoria'),
        ),
    ]

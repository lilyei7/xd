# Generated by Django 5.2.1 on 2025-05-29 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_insumocompuesto_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsumoElaborado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('unidad', models.CharField(max_length=50)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tiempo_preparacion', models.IntegerField(default=0, help_text='Tiempo en minutos')),
                ('metodo_preparacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'insumos_elaborados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='IngredienteInsumoElaborado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insumo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usado_en_elaborados', to='accounts.insumo')),
                ('insumo_compuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usado_en_elaborados', to='accounts.insumocompuesto')),
                ('insumo_elaborado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='accounts.insumoelaborado')),
            ],
            options={
                'db_table': 'ingredientes_insumo_elaborado',
                'constraints': [models.CheckConstraint(check=models.Q(
                    models.Q(insumo__isnull=False, insumo_compuesto__isnull=True) |
                    models.Q(insumo__isnull=True, insumo_compuesto__isnull=False)
                ), name='ingrediente_elaborado_solo_un_tipo')],
            },
        ),
    ]

# Generated by Django 5.2.1 on 2025-05-21 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_merge_20250521_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='codigo_interno',
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-16 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0007_alter_salida_orden_venta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recepcion',
            old_name='sku_in',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='recepcion',
            old_name='unidades_in',
            new_name='unidades',
        ),
        migrations.RenameField(
            model_name='salida',
            old_name='sku_out',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='salida',
            old_name='unidades_out',
            new_name='unidades',
        ),
    ]

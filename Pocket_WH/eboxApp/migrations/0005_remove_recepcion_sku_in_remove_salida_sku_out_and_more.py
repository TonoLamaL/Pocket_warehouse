# Generated by Django 4.1.5 on 2023-02-16 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0004_alter_inventario_unidades_alter_maestra_numero_sku_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recepcion',
            name='sku_in',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='sku_out',
        ),
        migrations.DeleteModel(
            name='Inventario',
        ),
        migrations.DeleteModel(
            name='Maestra',
        ),
        migrations.DeleteModel(
            name='Recepcion',
        ),
        migrations.DeleteModel(
            name='Salida',
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-24 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0016_recepcion_orden_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='sku_out',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eboxApp.maestra'),
        ),
    ]

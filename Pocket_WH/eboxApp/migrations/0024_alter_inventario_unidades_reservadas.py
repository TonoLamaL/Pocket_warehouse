# Generated by Django 4.1.7 on 2023-03-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0023_inventario_unidades_disponibles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='unidades_reservadas',
            field=models.IntegerField(default=0),
        ),
    ]
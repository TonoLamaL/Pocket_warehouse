# Generated by Django 4.1.7 on 2023-03-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0026_remove_inventario_unidades_reservadas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='unidades_reservadas',
            field=models.IntegerField(default=0),
        ),
    ]

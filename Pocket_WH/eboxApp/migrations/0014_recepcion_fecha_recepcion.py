# Generated by Django 4.1.7 on 2023-02-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0013_salida_fecha_despacho'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion',
            name='fecha_recepcion',
            field=models.DateField(null=True),
        ),
    ]

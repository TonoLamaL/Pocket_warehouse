# Generated by Django 4.1.7 on 2023-03-10 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0032_inventario_unidades_preparadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida',
            name='estado_anterior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estado_anterior_salida', to='eboxApp.estados'),
        ),
    ]

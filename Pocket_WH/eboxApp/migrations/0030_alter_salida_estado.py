# Generated by Django 4.1.7 on 2023-03-10 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0029_alter_inventario_unidades_reservadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eboxApp.estados'),
        ),
    ]
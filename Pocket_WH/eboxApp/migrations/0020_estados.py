# Generated by Django 4.1.7 on 2023-03-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboxApp', '0019_delete_detallerecepcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=300)),
            ],
        ),
    ]

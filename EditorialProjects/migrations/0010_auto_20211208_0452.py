# Generated by Django 3.2.5 on 2021-12-08 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EditorialProjects', '0009_alter_proyecto_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='encargado',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='entrega',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='importe',
        ),
    ]

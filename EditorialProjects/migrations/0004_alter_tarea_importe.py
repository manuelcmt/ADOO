# Generated by Django 3.2.5 on 2021-12-08 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EditorialProjects', '0003_tarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='importe',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]
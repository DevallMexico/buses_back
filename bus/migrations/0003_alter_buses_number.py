# Generated by Django 4.0.3 on 2022-04-14 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_buses_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buses',
            name='number',
            field=models.PositiveIntegerField(default=10, verbose_name='Numero'),
        ),
    ]

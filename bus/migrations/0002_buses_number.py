# Generated by Django 4.0.3 on 2022-04-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='number',
            field=models.PositiveIntegerField(default=10, verbose_name='Capacidad'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0009_auto_20161016_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_data_old',
            name='photolinks',
            field=models.ImageField(default='carsell/None/no-img.jpg', upload_to='carsell/'),
        ),
    ]

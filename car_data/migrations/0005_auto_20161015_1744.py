# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0004_auto_20161015_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_data_old',
            name='specifications',
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='brand',
            field=models.CharField(default='blah', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='confirmed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='fuel',
            field=models.CharField(default='null', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='reading',
            field=models.CharField(default='null', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='transmission',
            field=models.CharField(default='null', max_length=10),
            preserve_default=False,
        ),
    ]
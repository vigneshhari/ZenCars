# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0003_auto_20161015_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_data_new',
            name='id',
        ),
        migrations.RemoveField(
            model_name='car_data_old',
            name='id',
        ),
        migrations.AddField(
            model_name='car_data_new',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='Location',
            field=models.CharField(default='kochi', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car_data_new',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
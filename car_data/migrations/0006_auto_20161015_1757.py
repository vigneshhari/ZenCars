# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0005_auto_20161015_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_data_old',
            old_name='Body_type',
            new_name='body_type',
        ),
        migrations.AddField(
            model_name='car_data_old',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='Location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='features',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='general_information',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='hits',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='photolinks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='car_data_old',
            name='videolinks',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0011_auto_20161016_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='varient_data',
            old_name='Body_type',
            new_name='body_type',
        ),
        migrations.RemoveField(
            model_name='varient_data',
            name='milege',
        ),
        migrations.AddField(
            model_name='varient_data',
            name='hits',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='varient_data',
            name='main_car',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='varient_data',
            name='photolinks',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='varient_data',
            name='videolink',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0013_auto_20161016_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_review',
            name='user_name',
        ),
        migrations.AddField(
            model_name='car_review',
            name='car_type',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]

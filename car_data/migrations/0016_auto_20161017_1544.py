# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0015_auto_20161017_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_data_new',
            old_name='Body_type',
            new_name='body_type',
        ),
    ]

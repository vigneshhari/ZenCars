# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0018_auto_20161018_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_data_new',
            name='photolinks',
            field=models.TextField(),
        ),
    ]

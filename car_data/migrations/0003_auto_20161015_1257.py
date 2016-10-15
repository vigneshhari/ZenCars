# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_data', '0002_auto_20161014_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_data_old',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('car_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('photolinks', models.CharField(max_length=1000)),
                ('videolinks', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('features', models.TextField()),
                ('milege', models.CharField(max_length=10)),
                ('Body_type', models.CharField(max_length=20)),
                ('specifications', models.TextField()),
                ('general_information', models.TextField()),
                ('hits', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Car_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField()),
                ('content', models.TextField()),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='car_data_new',
            name='hits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
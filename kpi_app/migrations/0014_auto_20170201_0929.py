# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-01 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_app', '0013_auto_20170201_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricdata',
            name='denominator',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-13 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensionParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpi_app.Company')),
            ],
        ),
        migrations.RemoveField(
            model_name='dimension',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='dimension',
            name='dim_type',
        ),
        migrations.AddField(
            model_name='dimension',
            name='dim_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kpi_app.DimensionParent'),
            preserve_default=False,
        ),
    ]

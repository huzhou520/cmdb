# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-17 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='cpu_host',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Host', verbose_name='CPU对应的主机'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20160804_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='PENDING', max_length=30, verbose_name='Status'),
        ),
    ]

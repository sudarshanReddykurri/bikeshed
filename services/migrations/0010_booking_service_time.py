# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_booking_schedule_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='service_time',
            field=models.IntegerField(blank=True, choices=[(0, '9-10A.M'), (1, '10-11AM'), (2, '11-12AM'), (3, '12-1PM'), (4, '1-2PM'), (5, '2-3PM'), (6, '3-4PM'), (7, '4-5PM'), (8, '5-6PM')], default=0),
        ),
    ]

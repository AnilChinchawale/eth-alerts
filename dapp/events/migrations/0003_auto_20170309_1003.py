# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170308_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventvalue',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_values', to='events.Event'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='abi',
        ),
    ]

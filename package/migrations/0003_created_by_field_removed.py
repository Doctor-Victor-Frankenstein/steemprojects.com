# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_auto_20171119_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]

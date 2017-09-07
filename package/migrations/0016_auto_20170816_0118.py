# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0015_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo_url',
            field=models.URLField(blank=True, help_text='Enter your project repo hosting URL here. Example: https://github.com/opencomparison/opencomparison', null=True, unique=True, verbose_name='Source Code Repository URL'),
        ),
    ]
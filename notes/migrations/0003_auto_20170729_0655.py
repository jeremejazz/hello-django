# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20170729_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=129),
        ),
    ]

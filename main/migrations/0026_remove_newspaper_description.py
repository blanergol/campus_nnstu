# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_newspaper_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspaper',
            name='description',
        ),
    ]

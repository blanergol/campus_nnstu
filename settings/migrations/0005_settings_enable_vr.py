# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-02 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20170902_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='enable_vr',
            field=models.BooleanField(default=True, verbose_name='Виртуальная приемная активирована'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-03 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0019_settings_link_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='description_newspaper',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание раздела Газета'),
        ),
    ]

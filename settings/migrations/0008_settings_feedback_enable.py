# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-09 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_settings_img_slide_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='feedback_enable',
            field=models.BooleanField(default=True, verbose_name='Активировать обратну свзяь'),
        ),
    ]

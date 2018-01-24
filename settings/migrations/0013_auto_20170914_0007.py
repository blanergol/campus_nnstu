# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-13 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_auto_20170913_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='description_footer',
        ),
        migrations.AlterField(
            model_name='settings',
            name='short_about',
            field=models.TextField(default='', max_length=400, verbose_name='Краткое описание'),
        ),
    ]
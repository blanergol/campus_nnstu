# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20171127_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='', max_length=300, verbose_name='Заголовок слайдера'),
        ),
    ]
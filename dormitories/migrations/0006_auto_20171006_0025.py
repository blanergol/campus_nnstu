# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormitories', '0005_auto_20170917_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormitories',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='Описание'),
        ),
    ]

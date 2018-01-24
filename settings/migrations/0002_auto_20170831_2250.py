# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='description',
            field=models.TextField(default='', max_length=500, verbose_name='Описаие сайта'),
        ),
        migrations.AddField(
            model_name='settings',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='Название сайта'),
        ),
    ]

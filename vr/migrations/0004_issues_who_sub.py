# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-27 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr', '0003_issues_date_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='who_sub',
            field=models.CharField(default='', max_length=300, verbose_name='Рубрика'),
        ),
    ]

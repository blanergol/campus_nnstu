# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20171019_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='student_unification',
            field=models.BooleanField(default=False, verbose_name='Студенческие объединения'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-17 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0017_auto_20170917_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='description_student_council',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='description_student_starostat',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-07 17:52
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20171027_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='time_work',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300, verbose_name='Приемные часы'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-09 18:57
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170908_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='text',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Описание'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-07 23:02
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_leadership',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Руководство'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_ssg',
            field=ckeditor.fields.RichTextField(default='', verbose_name='ССГ'),
        ),
    ]
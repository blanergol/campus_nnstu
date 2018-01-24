# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-17 15:00
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0016_auto_20170917_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='description_student_starostat',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Текст для старостата'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='description_student_council',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Текст для студсовета студгородка'),
        ),
    ]
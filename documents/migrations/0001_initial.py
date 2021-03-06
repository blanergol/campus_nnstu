# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-10 20:50
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(default='', verbose_name='Описание')),
                ('file', models.FileField(default='', upload_to='', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Файлы',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]

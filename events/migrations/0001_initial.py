# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-09 20:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(default='', verbose_name='Описание')),
                ('location', models.CharField(default='', max_length=100, verbose_name='Локация')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('time_start', models.TimeField(default=django.utils.timezone.now, verbose_name='Время начала')),
                ('time_end', models.TimeField(default=django.utils.timezone.now, verbose_name='Время конца')),
            ],
            options={
                'verbose_name': 'Мероприятия',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]

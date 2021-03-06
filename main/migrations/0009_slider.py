# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-13 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170911_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Текст на слайде')),
                ('button_text', models.CharField(default='', max_length=20, verbose_name='Текст на кнопке')),
                ('button_link', models.CharField(default='', max_length=20, verbose_name='Ссылка на кнпоке (Напрмер: contact, без домена сайта)')),
                ('img', models.FileField(upload_to='', verbose_name='Фотография')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20170918_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название(выпуск)')),
                ('img', models.FileField(upload_to='', verbose_name='Картика')),
                ('file', models.FileField(max_length=300, upload_to='', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Газета',
                'verbose_name_plural': 'Газета',
            },
        ),
    ]

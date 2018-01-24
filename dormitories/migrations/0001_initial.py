# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-17 16:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0013_auto_20170917_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Название общежития')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание для общежития')),
                ('location', models.TextField(default='', verbose_name='Координаты')),
                ('employees', models.ManyToManyField(to='main.Employees', verbose_name='Старостат')),
            ],
            options={
                'verbose_name': 'Общежития',
                'verbose_name_plural': 'Общежития',
            },
        ),
        migrations.CreateModel(
            name='DormitoriesImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('img', models.FileField(upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Фотографии общежитий',
                'verbose_name_plural': 'Фотографии общежитий',
            },
        ),
        migrations.AddField(
            model_name='dormitories',
            name='images',
            field=models.ManyToManyField(to='dormitories.DormitoriesImg', verbose_name='Фото общежитий'),
        ),
    ]

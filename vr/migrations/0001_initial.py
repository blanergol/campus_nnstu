# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 19:36
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(default='', max_length=100, verbose_name='Email')),
                ('phone', models.CharField(default='', max_length=30, verbose_name='Телефон')),
                ('who', models.CharField(default='', max_length=100, verbose_name='Кто по отношению к НГТУ')),
                ('subject', models.CharField(default='', max_length=200, verbose_name='Тема')),
                ('question', models.TextField(default='', max_length=500, verbose_name='Вопрос')),
                ('answer', ckeditor.fields.RichTextField(max_length=2000, verbose_name='Ответ')),
                ('type', models.BooleanField(default=False, verbose_name='Обращение')),
                ('publication', models.BooleanField(default=False, verbose_name='Публикация вопроса')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата вопроса')),
                ('comments', models.BooleanField(default=False, verbose_name='Разрешить обсуждение вопроса')),
                ('employees', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Employees', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Вопросы',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]

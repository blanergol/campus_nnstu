# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-17 15:11
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170913_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCouncil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=300, verbose_name='Группа')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Студсовет студгородка',
                'verbose_name_plural': 'Студсовет студгородка',
            },
        ),
        migrations.RemoveField(
            model_name='employees',
            name='type',
        ),
        migrations.AddField(
            model_name='studentcouncil',
            name='employee',
            field=models.ManyToManyField(to='main.Employees', verbose_name='Работники'),
        ),
    ]

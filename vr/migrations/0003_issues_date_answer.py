# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vr', '0002_remove_issues_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='date_answer',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата ответа'),
        ),
    ]

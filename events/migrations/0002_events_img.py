# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-09 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='img',
            field=models.FileField(default='', upload_to='', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_employees_student_unification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='student_unification',
            new_name='student_unification_status',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedMe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directory',
            old_name='email',
            new_name='netid',
        ),
    ]

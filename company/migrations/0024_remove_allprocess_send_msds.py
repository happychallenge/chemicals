# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0023_auto_20170505_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allprocess',
            name='send_MSDS',
        ),
    ]
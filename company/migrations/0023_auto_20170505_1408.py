# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0022_auto_20170505_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allprocess',
            name='pallet_cbm',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='包装后托盘和CBM'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20170504_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.CharField(choices=[('T', '무역'), ('P', '생산'), ('M', '생산무역겸임')], default='P', max_length=1),
        ),
    ]

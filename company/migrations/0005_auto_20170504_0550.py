# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20170504_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='homepage',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20170504_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyproduct',
            name='price',
            field=models.FloatField(),
        ),
    ]

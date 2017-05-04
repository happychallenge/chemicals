# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20170504_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyproduct',
            name='exchange_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyproduct',
            name='rmb_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyproduct',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20170504_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='atomic_amount',
            field=models.FloatField(verbose_name='분자량'),
        ),
    ]

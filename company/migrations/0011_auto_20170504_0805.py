# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_companyproduct_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Address'),
        ),
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.CharField(choices=[('T', '무역'), ('P', '생산'), ('M', '생산무역겸임')], default='P', max_length=1, verbose_name='생산여부'),
        ),
        migrations.AlterField(
            model_name='company',
            name='en_name',
            field=models.CharField(max_length=50, verbose_name='영문이름'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=30, verbose_name='중문이름'),
        ),
    ]

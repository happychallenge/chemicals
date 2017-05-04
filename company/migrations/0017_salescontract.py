# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0016_auto_20170504_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sales_amount', models.IntegerField()),
                ('contract_unitprice', models.FloatField()),
                ('currency', models.CharField(choices=[('D', 'US$'), ('R', 'RMB')], default='D', max_length=1)),
                ('packaging', models.CharField(max_length=100)),
                ('portofloading', models.CharField(max_length=100, verbose_name='선적항구')),
                ('portofdestination', models.CharField(max_length=100, verbose_name='도착항구')),
                ('devliveryrequest', models.CharField(blank=True, max_length=50, null=True, verbose_name='기타요구사항')),
                ('shipping_at', models.DateTimeField(verbose_name='선적일자')),
                ('contracted_at', models.DateTimeField(verbose_name='계약일자')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Product')),
            ],
        ),
    ]
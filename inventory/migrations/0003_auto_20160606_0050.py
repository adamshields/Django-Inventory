# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20160606_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Manufacturer', verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_stock_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.StockStatus', verbose_name='Stock Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170224_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='/home/joao/Desktop/djangoProjects/webstore/products/static/products/img'),
        ),
    ]

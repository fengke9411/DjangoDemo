# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.IntegerField(),
        ),
    ]

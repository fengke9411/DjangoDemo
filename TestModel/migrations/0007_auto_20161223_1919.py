# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 11:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0006_auto_20161223_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatarToken',
        ),
        migrations.RemoveField(
            model_name='user',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='user',
            name='skillTree',
        ),
        migrations.RemoveField(
            model_name='user',
            name='workExperience',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

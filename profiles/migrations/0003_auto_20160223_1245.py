# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='description default'),
        ),
    ]

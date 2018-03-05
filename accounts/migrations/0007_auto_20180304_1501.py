# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180304_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
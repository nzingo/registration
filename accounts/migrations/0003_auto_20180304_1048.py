# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180301_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

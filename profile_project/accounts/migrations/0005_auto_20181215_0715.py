# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-12-15 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181213_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='/media/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-07-07 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0003_auto_20190707_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='hashTg',
            new_name='hashTagText',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-07-08 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20190706_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parentTweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet'),
        ),
    ]

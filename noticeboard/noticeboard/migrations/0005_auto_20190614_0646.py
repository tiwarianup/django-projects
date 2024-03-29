# Generated by Django 2.2.2 on 2019-06-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0004_notice_noticeslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='noticeBody',
            field=models.TextField(max_length=240),
        ),
        migrations.AlterField(
            model_name='notice',
            name='noticeSlug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='noticeTitle',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='notice',
            name='noticeType',
            field=models.CharField(max_length=10),
        ),
    ]

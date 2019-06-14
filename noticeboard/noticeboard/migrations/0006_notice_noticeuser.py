# Generated by Django 2.2.2 on 2019-06-14 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticeboard', '0005_auto_20190614_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='noticeUser',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

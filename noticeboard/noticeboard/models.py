from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class notice(models.Model):
    noticeUser  = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    noticeTitle = models.CharField(max_length=25)
    noticeSlug  = models.SlugField(unique=True)
    noticeType  = models.CharField(max_length=10)
    noticeBody  = models.TextField(max_length=240)

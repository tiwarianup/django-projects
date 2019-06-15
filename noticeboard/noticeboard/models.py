from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class noticeQuerySet(models.QuerySet):

    def published(self):
        now = timezone.now()
        return self.filter(publishDate__lte=now) 

class noticeManager(models.Manager):

    def get_queryset(self):
        return noticeQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

        #return self.get_queryset().filter(publishDate__lte=now) # Here get_queryset() results in notice.objects

class notice(models.Model):
    noticeUser  = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    noticeTitle = models.CharField(max_length=25)
    noticeImage = models.ImageField(upload_to='images/', blank=True, null=True)
    noticeSlug  = models.SlugField(unique=True)
    noticeType  = models.CharField(max_length=10)
    noticeBody  = models.TextField(max_length=240)
    publishDate = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updateDate  = models.DateTimeField(auto_now=True)

    objects = noticeManager()

    class Meta:
        ordering = ['-publishDate', '-updateDate', '-timestamp']

    def postUrl(self):
        return f"/notice/notice-details/{self.noticeSlug}"
    
    def updateUrl(self):
        return f"/notice/update-notice/{self.noticeSlug}"

    def deleteUrl(self):
        return f"/notice/delete-notice/{self.noticeSlug}"


from django.db import models

from .utils import shortcodeGenerator, createShortCode
# Create your models here.

class ShortUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qsMain = super(ShortUrlManager, self).all(*args, **kwargs)
        qs = qsMain.filter(isActive=True)
        return qs

    def refreshShortcodes(self):
        qs = ShortUrl.objects.filter(pk__gte=1)
        newCodes = 0
        for q in qs:
            q.urlShortCode = createShortCode(q)
            print(q.urlShortCode)
            q.save()
            newCodes += 1
        return "New codes made: {i}".format(i=newCodes)
        


class ShortUrl(models.Model):
    inputUrl        = models.CharField(max_length=220)
    urlShortCode    = models.CharField(max_length=15, unique=True, blank=True)
    updateTime      = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    isActive        = models.BooleanField(default=True)

    objects = ShortUrlManager()

    def save(self, *args, **kwargs):
        #print("This is working!")
        if self.urlShortCode is None or self.urlShortCode == "":
            self.urlShortCode = createShortCode(self)
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.inputUrl)
    
    def __unicode__(self):
        return str(self.inputUrl)

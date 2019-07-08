from django.db import models
from django.urls import reverse_lazy

from tweets.models import Tweet

# Create your models here.

class HashTag(models.Model):
    hashTagText = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hashTagText

    def get_absolute_url(self):
        return reverse_lazy("hashtag", kwargs={"hashtag": self.hashTagText})
    

    def get_tweets(self):
        return Tweet.objects.filter(tweetText__icontains="#"+self.hashTagText)

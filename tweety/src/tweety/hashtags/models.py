from django.db import models
from django.urls import reverse_lazy

from tweets.models import Tweet
from .signals import parsed_hashtags
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


def parsed_hashtags_receiver(sender, hashtag_list, *args, **kwargs):
    if len(hashtag_list) > 0:
        for hashTag in hashtag_list:
            newHashTag, created = HashTag.objects.get_or_create(hashTagText=hashTag)

parsed_hashtags.connect(parsed_hashtags_receiver)
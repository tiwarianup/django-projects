from django.db import models
from django.conf import settings
from django.urls import reverse

from .validators import validateTweetText

class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        obj = self.model(
            parentTweet = parent_obj,
            author = user,
            tweetText = parent_obj.tweetText
        )
        obj.save()
        return obj


class Tweet(models.Model):
    parentTweet = models.ForeignKey("self", blank=True, null=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweetText   = models.CharField(max_length=140, validators=[validateTweetText])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
    

    def __str__(self):
        return str(self.tweetText)
    
    def get_absolute_url(self):
        return reverse("tweet:tweetDetailView", kwargs={"pk":self.pk})

    # def clean(self, *args, **kwargs): 
    #     tweetText = self.tweetText
    #     if tweetText == "anup":
    #         raise ValidationError("The tweet cannot have my name!")
    #     return super(Tweet, self).clean(*args, **kwargs)
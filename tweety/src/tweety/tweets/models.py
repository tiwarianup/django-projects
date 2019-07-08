import re
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save

from hashtags.signals import parsed_hashtags
from .validators import validateTweetText

class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parentTweet:
            ogParentTweet = parent_obj.parentTweet
        else:
            ogParentTweet = parent_obj 

        qs = self.get_queryset().filter(
                author=user, 
                parentTweet=ogParentTweet
            ).filter(
                timestamp__year = timezone.now().year,
                timestamp__month = timezone.now().month,
                timestamp__day = timezone.now().day
            )
        if qs.exists():
            return None

        obj = self.model(
            parentTweet = ogParentTweet,
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
    
    objects = TweetManager()
    

    def __str__(self):
        return str(self.tweetText)
    
    def get_absolute_url(self):
        return reverse("tweet:tweetDetailView", kwargs={"pk":self.pk})

    # def clean(self, *args, **kwargs): 
    #     tweetText = self.tweetText
    #     if tweetText == "anup":
    #         raise ValidationError("The tweet cannot have my name!")
    #     return super(Tweet, self).clean(*args, **kwargs)

def tweetSaveReceiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parentTweet:
        # notify a user
        userRegex = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(userRegex, instance.tweetText)
        #print(usernames)
        #send notification to user.

        hashTagRegex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hashTagRegex, instance.tweetText)
        #print(hashtags)
        #send hashtag signal to user.
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)




post_save.connect(tweetSaveReceiver, sender=Tweet)

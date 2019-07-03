from django.db import models
from django.conf import settings


from .validators import validateTweetText

class Tweet(models.Model):
    author    = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweetText = models.CharField(max_length=140, validators=[validateTweetText])
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.tweetText)

    # def clean(self, *args, **kwargs):
    #     tweetText = self.tweetText
    #     if tweetText == "anup":
    #         raise ValidationError("The tweet cannot have my name!")
    #     return super(Tweet, self).clean(*args, **kwargs)
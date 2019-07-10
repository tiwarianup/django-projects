from rest_framework import serializers
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class ParentTweetModelSerializer(serializers.ModelSerializer):
    author          = UserDisplaySerializer(read_only=True)
    date_display    = serializers.SerializerMethodField()
    timesince       = serializers.SerializerMethodField()
    tweetUrl        = serializers.SerializerMethodField()
    likes           = serializers.SerializerMethodField()
    didLike         = serializers.SerializerMethodField()

    
    class Meta:
        model = Tweet
        fields = ["id", "author", "tweetText", "timestamp", "date_display", "timesince", 'tweetUrl', 'likes' , 'didLike']

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%B %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_tweetUrl(self, obj):
        return obj.get_absolute_url()

    def get_didLike(self, obj):
        user = self.context.get("user")
        try:
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
        except:
            pass
        return False

    
    def get_likes(self, obj):
        return obj.liked.all().count()

    

class TweetModelSerializer(serializers.ModelSerializer):
    author          = UserDisplaySerializer(read_only=True)
    date_display    = serializers.SerializerMethodField()
    timesince       = serializers.SerializerMethodField()
    tweetUrl        = serializers.SerializerMethodField()
    parentTweet     = ParentTweetModelSerializer(read_only=True)
    likes           = serializers.SerializerMethodField()
    didLike         = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = [ "id", "author", "tweetText", "timestamp", "date_display", "timesince", 'tweetUrl', 'parentTweet', 'likes', 'didLike', 'isReply']
        #read_only_fields = ['isReply']

    def get_didLike(self, obj):
        user = self.context.get("user")
        try:
            if user.is_authenticated():
                if user in obj.liked.all():
                    return True
        except:
            pass
        return False

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%B %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_tweetUrl(self, obj):
        return obj.get_absolute_url()

    def get_likes(self, obj):
        return obj.liked.all().count()

    # def get_isRetweet(self, obj):
    #     if obj.parentTweet:
    #         return True
    #     return False
    
from rest_framework import serializers
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class ParentTweetModelSerializer(serializers.ModelSerializer):
    author          = UserDisplaySerializer(read_only=True)
    date_display    = serializers.SerializerMethodField()
    timesince       = serializers.SerializerMethodField()
    tweetUrl        = serializers.SerializerMethodField()

    
    class Meta:
        model = Tweet
        fields = ["id", "author", "tweetText", "timestamp", "date_display", "timesince", 'tweetUrl']

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%B %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_tweetUrl(self, obj):
        return obj.get_absolute_url()

    

class TweetModelSerializer(serializers.ModelSerializer):
    author          = UserDisplaySerializer(read_only=True)
    date_display    = serializers.SerializerMethodField()
    timesince       = serializers.SerializerMethodField()
    tweetUrl        = serializers.SerializerMethodField()
    parentTweet     = ParentTweetModelSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ["id", "author", "tweetText", "timestamp", "date_display", "timesince", 'tweetUrl', 'parentTweet']

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%B %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
    def get_tweetUrl(self, obj):
        return obj.get_absolute_url()

    # def get_isRetweet(self, obj):
    #     if obj.parentTweet:
    #         return True
    #     return False
    
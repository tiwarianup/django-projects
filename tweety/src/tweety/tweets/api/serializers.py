from rest_framework import serializers
from django.utils.timesince import timesince
from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
    author = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = [ "author", "tweetText", "timestamp", "date_display", "timesince"]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%B %d %Y, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
    
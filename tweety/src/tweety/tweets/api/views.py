from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from tweets.models import Tweet
from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer

class RetweetApiView(APIView):
    permission_classes = [ permissions.IsAuthenticated ]

    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "This function is not allowed."
        if tweet_qs.exists() and tweet_qs.count() == 1:
            if request.user.is_authenticated():
                newTweet = Tweet.objects.retweet(request.user, tweet_qs.first())
                if newTweet is not None:
                    data = TweetModelSerializer(newTweet).data
                    return Response(data)
                message = "Cannot retweet the same tweet within 1 day."
        return Response({"response": message}, status=400)

class TweetCreateApiView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        userFollowing = self.request.user.profile.get_following()
        qs1 = Tweet.objects.filter(author__in=userFollowing).order_by("-timestamp")
        qs2 = Tweet.objects.filter(author=self.request.user)
        qs = (qs1 | qs2).distinct().order_by("-timestamp")
        #qs = Tweet.objects.all().order_by("-timestamp")
        #print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(tweetText__icontains=query) |
                Q(author__username__icontains=query) 
            )
        return qs

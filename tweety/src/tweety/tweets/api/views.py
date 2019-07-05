from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions

from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetCreateApiView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        qs = Tweet.objects.all().order_by("-timestamp")
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(tweetText__icontains=query) |
                Q(author__username__icontains=query) 
            )
        return qs

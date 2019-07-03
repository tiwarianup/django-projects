
from django.conf.urls import url
from .views import TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='tweetListView'),
    url(r'^create/$', TweetCreateView.as_view(), name='tweetCreateView'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='tweetDetailView'),
    url(r'^(?P<pk>\d+)/edit/$', TweetUpdateView.as_view(), name='tweetUpdateView'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='tweetDeleteView'),
    # $ means the end of the string
]
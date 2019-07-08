from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import TweetListApiView, TweetCreateApiView, RetweetApiView


urlpatterns = [
    url(r'^$', TweetListApiView.as_view(), name='list'),
    url(r'^create/$', TweetCreateApiView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetApiView.as_view(), name='retweet'),
]
from django.conf.urls import url
from django.views.generic.base import RedirectView

from tweets.api.views import TweetListApiView

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweets/$', TweetListApiView.as_view(), name='list'),
]
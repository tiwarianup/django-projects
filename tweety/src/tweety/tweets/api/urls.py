from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import TweetListApiView, TweetCreateApiView


urlpatterns = [
    url(r'^$', TweetListApiView.as_view(), name='list'),
    url(r'^create/$', TweetCreateApiView.as_view(), name='create'),
]
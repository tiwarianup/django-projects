from django.views.generic.base import RedirectView
from django.conf.urls import url
from .views import UserDetailView, UserFollowView


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='details'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'),
    
    # $ means the end of the string
]
from django.views.generic.base import RedirectView
from django.conf.urls import url
from .views import UserDetailView


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='details'),
    
    # $ means the end of the string
]
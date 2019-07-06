from django.views.generic.base import RedirectView
from django.conf.urls import url
from .views import UserDetailView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='list'),
    
    # $ means the end of the string
]
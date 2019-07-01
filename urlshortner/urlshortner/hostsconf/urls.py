from django.conf.urls import url
from .views import other

urlpatterns = [
    url(r'^(?P<path>.*)', other),

]

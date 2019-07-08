from django.shortcuts import render
from django.views import View


# Create your views here.

from .models import HashTag

class HashTagView(View):
    def get(self, request, hashtag, *args, **kwargs):
        obj, created = HashTag.objects.get_or_create(hashTagText=hashtag)
        return render(request, "hashtags/hashTagView.html", {"object": obj})
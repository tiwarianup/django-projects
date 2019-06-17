from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from .models import ShortUrl

# Create your views here.

def redirectView(request, urlShortCode=None, *args, **kwargs):
    obj = get_object_or_404(ShortUrl, urlShortCode=urlShortCode)
    return HttpResponseRedirect(obj.inputUrl)

class redirectCBView(View):
    def get(self, request, urlShortCode=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, urlShortCode=urlShortCode)
        return HttpResponseRedirect(obj.inputUrl)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(None)
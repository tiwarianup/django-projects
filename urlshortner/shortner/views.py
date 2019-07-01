from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.conf import settings


from .models import ShortUrl
from .forms import SubmitUrlForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "title": "SHORTEN URLs EASILY",
            "form" :  form
        }
        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)

        context = {
            "title": "SHORTEN URLs EASILY",
            "form" :  form
        }

        template = "home.html"

        if form.is_valid():
            submittedUrl = form.cleaned_data.get('inputUrl')
            obj, created = ShortUrl.objects.get_or_create(inputUrl=submittedUrl)

            DEFAULT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL', 'http://www.a.su')
            SITE_URL = DEFAULT_URL.split(".")[1:]
            print(SITE_URL)
            SITE_URL = "".join(SITE_URL)

            context = {
                "title": "SHORTEN URLs EASILY",
                "toShort" : submittedUrl,
                "objects" : obj,
                "created" : created,
                "siteUrl" : SITE_URL
            }

            if created:
                template = "success.html"
            else:
                template = "already-exists.html"

        return render(request, template, context)

def redirectView(request, urlShortCode=None, *args, **kwargs):
    obj = get_object_or_404(ShortUrl, urlShortCode=urlShortCode)
    return HttpResponseRedirect(obj.inputUrl)

class RedirectCBView(View):
    def get(self, request, urlShortCode=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, urlShortCode=urlShortCode)
        return HttpResponseRedirect(obj.inputUrl)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(None)
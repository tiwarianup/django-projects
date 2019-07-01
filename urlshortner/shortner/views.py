from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

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

            context["toShort"] = form.cleaned_data.get("inputUrl")
            inputUrl = form.cleaned_data.get('inputUrl')
            obj, created = ShortUrl.objects.get_or_create(inputUrl=inputUrl)

            if created:
                context['object'] = obj
                context['created'] = created
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
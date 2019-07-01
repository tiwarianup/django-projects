from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL', 'http://www.a.su')

def other(request, path=None):
    newUrl = DEFAULT_REDIRECT_URL
    if path is not None:
        newUrl = DEFAULT_REDIRECT_URL + '/' + path
    return HttpResponseRedirect(newUrl)
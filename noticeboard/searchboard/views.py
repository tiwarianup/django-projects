from django.shortcuts import render
from .models import SearchQuery

from noticeboard.models import notice
# Create your views here.

def searchPage(request):
    query = request.GET.get('q', None)
    context = {"query": query}
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        qs = notice.objects.searchNotice(query)
        context = {"query": query, "foundNotices": qs}
    return render(request, "searchPage.html", context)
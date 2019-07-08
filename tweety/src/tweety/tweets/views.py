from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views import View

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            newTweet = Tweet.objects.retweet(request.user, tweet)
            if newTweet is not None:
                #return HttpResponseRedirect(newTweet.get_absolute_url())
                return HttpResponseRedirect('/')
        #return HttpResponseRedirect(tweet.get_absolute_url())
        return HttpResponseRedirect('/')


class TweetCreateView( FormUserNeededMixin, CreateView):
    
    form_class = TweetModelForm
    #success_url = reverse_lazy("tweet:tweetDetailView")
    template_name = "tweets/createView.html"
    
    #login_url = '/admin/'
    #model = Tweet
    #fields = ["tweetText"]

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.author = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to Tweet!"])
    #         return self.form_invalid(form)

class TweetUpdateView(UserOwnerMixin, LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    #success_url = reverse_lazy("tweet:tweetDetailView")
    template_name = "tweets/updateView.html"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:tweetListView")
    template_name = "tweets/deleteView.html"
    

class TweetDetailView(DetailView):
    template_name = 'tweets/detailView.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, id=pk)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(TweetDetailView, self).get_context_data(*args, **kwargs)
        #context['anotherList'] =  Tweet.objects.all() #change the context object names
        #print(context)
        return context

class TweetListView(ListView):
    template_name = 'tweets/listView.html'
    
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(tweetText__icontains=query) |
                Q(author__username__icontains=query) 
            )
        return qs
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet-api:create')
        #print(context)
        return context


# def tweetDetailsView(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     return render(request, 'tweets/detailView.html', {"object": obj})

# def tweetListView(request):
#     querySet = Tweet.objects.all()
#     print(querySet)
#     return render(request, 'tweets/listView.html', {"object_list": querySet})

# def tweetCreateViewfn(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.author = request.user
#         instance.save()
    
#     context = { "form" : form }
#     return render(request, "tweets/createView.html", context)
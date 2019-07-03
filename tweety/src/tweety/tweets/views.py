from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.

class TweetCreateView( FormUserNeededMixin, CreateView):
    
    form_class = TweetModelForm
    success_url = "/tweet/"
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
    success_url = '/tweet/'
    template_name = "tweets/updateView.html"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("home")
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
    queryset = Tweet.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
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
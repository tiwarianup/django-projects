from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.views import View

from .forms import UserRegisterForm
from .models import UserProfile

User = get_user_model()

class UserRegisterView(FormView):
    template_name = 'accounts/userRegisterForm.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        print(dir(form))
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = User.objects.create(username=username, email=email)
        newUser.set_password(password)
        newUser.save()
        return super(UserRegisterView, self).form_valid(form)

# Create your views here.
class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/userDetail.html'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))
    
    # def get_slug_field(self):
    #     return "username"

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context["following"] = UserProfile.objects.isFollwoing(self.request.user, self.get_object())
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context
    

class UserFollowView(View):

    def get(self, request, username, *args, **kwargs):
        toggleUser = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            isFollowing = UserProfile.objects.toggleFollow(request.user, toggleUser)

        return redirect("profiles:details", username=username)
        # url = reverse('profiles:details', kwargs={"username": username})
        # HttpResponseRedirect(url)
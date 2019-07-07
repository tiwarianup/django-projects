from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.views import View

User = get_user_model()

# Create your views here.
class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/userDetail.html'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))
    
    # def get_slug_field(self):
    #     return "username"

class UserFollowView(View):

    def get(self, request, username, *args, **kwargs):
        toggleUser = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            userProfile = request.user.profile

        return redirect("profiles:details", kwargs={"username": username})
        # url = reverse('profiles:details', kwargs={"username": username})
        # HttpResponseRedirect(url)
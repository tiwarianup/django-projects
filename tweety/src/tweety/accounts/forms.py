from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPwd = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_conformPwd(self):
        password = self.cleaned_data.get("password")
        confirmPwd = self.cleaned_data.get("confirmPwd")
        if password != confirmPwd:
            raise forms.ValidationError("Password are not matching, please check.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
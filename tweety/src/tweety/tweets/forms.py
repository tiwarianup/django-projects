from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    tweetText = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your Tweet here.', 'class': 'form-control'}), label='')
    class Meta:
        model = Tweet
        fields = [ 
        #    "author", 
        "tweetText"
        ]

    def clean_tweetText(self, *args, **kwargs):
        tweetText = self.cleaned_data.get("tweetText")
        if tweetText == "anup":
            raise forms.ValidationError("The tweet cannot be my name!")
        return tweetText
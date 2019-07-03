from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
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
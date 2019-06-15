from django import forms
from .models import notice

class createNoticeForm(forms.Form):
    noticeTitle = forms.CharField()
    noticeSlug  = forms.SlugField()
    noticeType  = forms.CharField()
    noticeBody  = forms.CharField(widget=forms.Textarea)

class createNoticeModelForm(forms.ModelForm):
    class Meta:
        model = notice
        fields = ['noticeTitle', 'noticeSlug', 'noticeType', 'noticeBody', 'publishDate', 'noticeImage']

    def clean_noticeType(self, *args, **kwargs):
        allowedTypes = ["LOST", "FOUND", "BUY", "SELL"]
        noticeType = self.cleaned_data.get('noticeType')
        if noticeType not in allowedTypes:
            raise forms.ValidationError('This type of Notice is not allowed. Please check spellings. Allowed Types: "LOST", "FOUND", "BUY", "SELL"')
        return noticeType


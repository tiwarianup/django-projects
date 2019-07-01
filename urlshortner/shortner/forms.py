from django import forms
from .validators import validate_anup, validate_inputUrl

class SubmitUrlForm(forms.Form):
    inputUrl = forms.CharField(label='Submit URL', validators = [ validate_inputUrl, validate_anup ])

    """ def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()

    def clean_inputUrl(self):
        url = self.cleaned_data['inputUrl']
        urlValidator = URLValidator()
        try:
            urlValidator(url)
        except :
            raise forms.ValidationError("Invalid URL for this field.")
        return url """
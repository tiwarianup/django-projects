from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.author = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to Tweet!"])
            return self.form_invalid(form)

class UserOwnerMixin(FormUserNeededMixin, object):

    def form_valid(self, form):
        if form.instance.author == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You are not allowed to update this Tweet!"])
            return self.form_invalid(form)
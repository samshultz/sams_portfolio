from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):

    fullname = forms.CharField(label=_("Full Name"), max_length=50)
    email = forms.EmailField(label=_("Your Email"))
    # phone = forms.CharField(_("Phone"), max_length=15)
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'rows': 5}))

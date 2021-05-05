from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


@require_POST
def contact(request):
    sent = False
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            send_mail(
                f"Message from {cd['fullname']}({cd['email']})", 
                cd['message'], settings.EMAIL_HOST_USER, 
                [settings.EMAIL_HOST_USER])
            sent = True
            return redirect("index")

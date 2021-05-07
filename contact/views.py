from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm


@require_POST
def contact(request):
    redirect_url = reverse('index') + "#contact"
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            send_mail(
                f"Message from {cd['fullname']}({cd['email']})", 
                cd['message'], settings.EMAIL_HOST_USER, 
                [settings.EMAIL_HOST_USER])
            messages.success(request, 'Your message has been sent to the admin. Expect a reply soon')
        else:
            messages.error(request, 'Correct the <strong>ERRORS</strong> below')
    return redirect(redirect_url)

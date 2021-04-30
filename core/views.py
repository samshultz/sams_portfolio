from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


class HomepageView(TemplateView):
    template_name = "core/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['user'] = User.objects.first()
        return context
    
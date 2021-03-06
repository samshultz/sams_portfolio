from django.shortcuts import render
from django.views.generic.base import TemplateView
from about_me.models import AboutMe
from .models import StackCategory


class HomepageView(TemplateView): # pragma: no cover
    template_name = "core/index.html"

    
    def get_context_data(self, **kwargs): 
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['about_me'] = AboutMe.objects.first()
        context['stack_categories'] = StackCategory.objects.all()
        
        return context
    
from django import template
from django.contrib.auth.models import User

from ..models import AboutMe

register = template.Library()

@register.inclusion_tag('core/dummy.html', takes_context=True)
def show_personal_details(context, template="about_me/about_me.html"):
	
	user_details = AboutMe.objects.first()
	
	return {'user_details': user_details, 'template': template}

@register.simple_tag()
def get_photo_url():
	about_me = AboutMe.objects.first()
	photo = about_me.photo if about_me else ""
	photo_url = photo.url if photo else ""
	return photo_url
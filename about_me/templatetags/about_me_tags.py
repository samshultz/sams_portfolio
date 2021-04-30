from django import template
from django.contrib.auth.models import User

from ..models import AboutMe

register = template.Library()

@register.inclusion_tag('core/dummy.html', takes_context=True)
def show_personal_details(context, template="about_me/about_me.html"):
	
	user_details = AboutMe.objects.first()
	
	return {'user_details': user_details, 'template': template}

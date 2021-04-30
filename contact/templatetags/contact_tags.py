from django import template
from ..forms import ContactForm

register = template.Library()

@register.inclusion_tag('core/dummy.html', takes_context=True)
def render_contact_form(context, template="contact/contact.html"):
	
	contact_form = ContactForm()
	
	return {'contact_form': contact_form, 'template': template}

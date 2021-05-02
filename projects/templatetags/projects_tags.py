from django import template
from ..models import Project, Category


register = template.Library()


@register.inclusion_tag('core/dummy.html', takes_context=True)
def list_projects(context, template="projects/projects.html"):
	
	projects = Project.objects.all()[:5]
	
	return {'projects': projects, 'template': template}


@register.inclusion_tag('core/dummy.html', takes_context=True)
def list_categories(context, template="projects/categories.html"):
	categories = Category.objects.all()
	return {'categories': categories, 'template': template}
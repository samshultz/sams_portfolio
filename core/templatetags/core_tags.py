from django import template
from ..models import Skill, WorkExperience, TechStack


register = template.Library()


@register.inclusion_tag('core/dummy.html', takes_context=True)
def list_skills(context, template="core/skills.html"):
	
	skills = Skill.objects.all()[:5]
	
	return {'skills': skills, 'template': template}


@register.inclusion_tag('core/dummy.html', takes_context=True)
def list_work_experiences(context, template="core/experience.html"):

	experiences = WorkExperience.objects.all()[:5]
	
	return {'experiences': experiences, 'template': template}


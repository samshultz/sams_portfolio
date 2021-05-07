from django.contrib.auth.models import User
from django.template import Context, Template

from .models import Category, Project

def test_str_representation_of_project(db):
    user = User.objects.create(
        username="john", 
        first_name="John", 
        last_name="Doe", 
        email="johndoe@email.com")
    project = Project.objects.create(
        user=user,
        name="Medwave care",
        description="A very long description",
        url="https://www.medwavecare.com"
    )
    assert "Medwave care" == str(project)

def test_str_representation_of_category(db):
    category = Category.objects.create(name="Health")
    assert "Health" == str(category)

def test_verbose_name_is_categories(db):
    assert Category._meta.verbose_name_plural == 'Categories'

def test_list_categories_templatetag(db):
    context = Context({'title': 'my_title'})
    category = Category.objects.create(name="Health")
    template_to_render = Template(
        '{% load projects_tags %}'
        '{% list_categories %}'
    )
    rendered_template = template_to_render.render(context)
    assert "Health" in rendered_template

def test_list_projects_templatetag(db):
    context = Context({'title': 'my_title'})
    user = User.objects.create(
        username="john", 
        first_name="John", 
        last_name="Doe", 
        email="johndoe@email.com")
    project = Project.objects.create(
        user=user,
        name="Medwave care",
        description="A very long description",
        url="https://www.medwavecare.com"
    )
    assert "Medwave care" == str(project)

    template_to_render = Template(
        '{% load projects_tags %}'
        '{% list_projects %}'
    )
    rendered_template = template_to_render.render(context)
    assert "Medwave care" in rendered_template
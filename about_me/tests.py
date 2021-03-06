import time
import os

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.template import Context, Template

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from django_webtest import WebTest
import pytest

from .models import AboutMe

@pytest.fixture
def about_me(db):
    user = User.objects.create(
        username="john", 
        first_name="John", 
        last_name="Doe", 
        email="johndoe@email.com")
    about_me = AboutMe.objects.create(user=user, description="A really long text", phone="489478848")

    return about_me


def test_str_representation_of_about_me(about_me, db):
    assert "John Doe" == str(about_me)

def test_only_one_instance_can_be_saved(about_me, db):
    user = User.objects.create(
        username="jrhn", 
        first_name="Caleb", 
        last_name="Doe", 
        email="calebdoe@email.com")
    with pytest.raises(ValidationError):
        about_me = AboutMe.objects.create(user=user, description="A really long text", phone="48934478848")


def test_email_property_return_email(about_me, db):
    assert about_me.email == "johndoe@email.com"

def test_fullname_property_return_fullname(about_me, db):
    assert about_me.fullname == "John Doe"

def test_show_personal_details_templatetag(db, about_me):
    context = Context({'title': 'my_title'})
    template_to_render = Template(
        '{% load about_me_tags %}'
        '{% show_personal_details %}'
    )
    rendered_template = template_to_render.render(context)
    assert "489478848" in rendered_template


# def test_user_details_display_on_page(about_me, db, django_app):
#     capabilities = DesiredCapabilities.FIREFOX.copy()
#     username = os.environ["SAUCE_USERNAME"]
#     access_key = os.environ["SAUCE_ACCESS_KEY"]
#     capabilities["tunnel-identifier"] = os.environ.get("TRAVIS_JOB_NUMBER", "20.1")
#     hub_url = f"{username}:{access_key}@ondemand.eu-central-1.saucelabs.com:443"
#     browser = webdriver.Remote(desired_capabilities=capabilities, command_executor="https://%s/wd/hub" % hub_url)

#     time.sleep(5)

#     about = browser.find_element_by_id('about-menu-item')
#     about.click()
#     time.sleep(5)
#     name = browser.find_element_by_id('name-box').text
#     assert name != ""
#     assert "Personal Information" in browser.page_source
#     time.sleep(3)
#     browser.quit()
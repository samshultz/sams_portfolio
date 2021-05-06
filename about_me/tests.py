import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
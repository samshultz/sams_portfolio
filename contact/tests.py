import os
import time
import pytest

from django.template import Context, Template
from django_webtest import WebTest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# @pytest.fixture
# def setup_browser():
#     capabilities = DesiredCapabilities.FIREFOX.copy()
#     username = os.environ["SAUCE_USERNAME"]
#     access_key = os.environ["SAUCE_ACCESS_KEY"]
#     capabilities["tunnel-identifier"] = os.environ.get("TRAVIS_JOB_NUMBER", "20.1")
#     hub_url = f"{username}:{access_key}@ondemand.eu-central-1.saucelabs.com:443"
#     browser = webdriver.Remote(desired_capabilities=capabilities, command_executor="https://%s/wd/hub" % hub_url)

#     return browser


# def test_invalid_form(db, setup_browser):
#     time.sleep(4)

#     setup_browser.find_element_by_id('contact-menu-item').click()
#     time.sleep(2)

#     fullname = setup_browser.find_element_by_id("id_fullname").send_keys("Jason Atwood")
#     email = setup_browser.find_element_by_id("id_email").send_keys("jatwood")
#     message = setup_browser.find_element_by_id("id_message").send_keys("Where was Hannah Wells deployed")
#     button = setup_browser.find_element_by_id("cf-submit").click()
#     time.sleep(3)
#     assert "Correct the <strong>ERRORS</strong> below" in setup_browser.page_source
#     setup_browser.quit()

# def test_valid_form(db, setup_browser):
#     time.sleep(4)

#     setup_browser.find_element_by_id('contact-menu-item').click()
#     time.sleep(2)

#     fullname = setup_browser.find_element_by_id("id_fullname").send_keys("Jason Atwood")
#     email = setup_browser.find_element_by_id("id_email").send_keys("jatwood@email.com")
#     message = setup_browser.find_element_by_id("id_message").send_keys("Where was Hannah Wells deployed")
#     button = setup_browser.find_element_by_id("cf-submit").click()
#     time.sleep(3)
#     assert "Your message has been sent to the admin. Expect a reply soon" in setup_browser.page_source

#     setup_browser.quit()

def test_render_contact_form_templatetag(db):
    context = Context({'title': 'my_title'})
    template_to_render = Template(
        '{% load contact_tags %}'
        '{% render_contact_form %}'
    )
    rendered_template = template_to_render.render(context)
    assert "Full Name" in rendered_template
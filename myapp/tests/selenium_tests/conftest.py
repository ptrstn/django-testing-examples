import pytest
from django.contrib.auth.hashers import make_password
from selenium import webdriver

TEST_USERNAME = "example"
TEST_PASSWORD = "VerySecurePasswort"


@pytest.fixture
def firefox():
    """returns a Firefox browser webdriver instance"""
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    firefox_webdriver = webdriver.Firefox(firefox_options=options)
    firefox_webdriver.implicitly_wait(10)
    yield firefox_webdriver
    firefox_webdriver.quit()


@pytest.fixture
def user(django_user_model):
    """returns an User object"""
    return django_user_model.objects.create(
        username=TEST_USERNAME,
        password=make_password(TEST_PASSWORD)
    )

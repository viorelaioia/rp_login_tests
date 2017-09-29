import pytest
import pyotp
import requests


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def ldap(variables):
    return variables['ldap_user']


@pytest.fixture
def passcode(secret_seed, counter_api):
    r = requests.get(counter_api)
    counter = r.json()
    hotp = pyotp.HOTP(secret_seed)
    return hotp.at(counter)


@pytest.fixture
def urls(variables):
    return variables['RPs_urls']


@pytest.fixture
def counter_api(variables):
    return variables['counter_API_endpoint']

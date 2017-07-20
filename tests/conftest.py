import pytest
import pyotp


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def ldap(variables):
    return variables['ldap_user']


@pytest.fixture
def passcode(secret_seed):
    totp = pyotp.TOTP(secret_seed)
    return totp.now()


@pytest.fixture
def urls(variables):
    return variables['RPs_urls']

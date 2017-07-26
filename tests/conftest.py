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
def passcode(secret_seed, counter):
    hotp = pyotp.HOTP(secret_seed)
    return hotp.at(counter+1)


@pytest.fixture
def urls(variables):
    return variables['RPs_urls']


@pytest.fixture
def write_in_file(filename, content):
    f = open(filename, 'w')
    f.write(str(content))
    f.close()


@pytest.fixture
def file_content(filename):
    if not open(filename, 'r').read():
        return 0
    return open(filename, 'r').read()

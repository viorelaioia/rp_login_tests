from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class TestRp(Base):
    _sign_in_button = (By.CSS_SELECTOR, '.btn-signin.btn-signin-red')
    _logout_button_locator = (By.CSS_SELECTOR, '#main-content a[href="/logout"]')

    def __init__(self, selenium, url):
        super(TestRp, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def login_with_ldap(self, email, password):
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

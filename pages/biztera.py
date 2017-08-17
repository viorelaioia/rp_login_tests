from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Biztera(Base):
    _login_button_locator = (By.CSS_SELECTOR, 'button.login-button')
    _name_locator = (By.CSS_SELECTOR, 'div[class*="display-name"]')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[bt-sign-out]')

    def __init__(self, selenium, url):
        super(Biztera, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_name_displayed(self):
        return self.is_element_visible(*self._name_locator)

    def login_with_ldap(self, email, password):
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password, ldap_only=True)
        return TwoFactorAuthentication(self.selenium)

    def logout(self):
        self.selenium.find_element(*self._name_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class SsoDashboard(Base):

    _profile_icon_locator = (By.CSS_SELECTOR, '.profile-icon')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href="/logout"]')

    def __init__(self, selenium, url):
        super(SsoDashboard, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_profile_icon_displayed(self):
        return self.is_element_visible(*self._profile_icon_locator)

    def login_with_ldap(self, email, password):
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)

    def logout(self):
        self.selenium.find_element(*self._profile_icon_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

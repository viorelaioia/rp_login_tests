from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Discourse(Base):
    _login_button_locator = (By.CSS_SELECTOR, 'button.login-button')
    _avatar_image_locator = (By.CSS_SELECTOR, '#current-user a[class="icon"]')
    _logout_button_locator = (By.CSS_SELECTOR, '.widget-link.logout')

    def __init__(self, selenium, url):
        super(Discourse, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_avatar_displayed(self):
        return self.is_element_visible(*self._avatar_image_locator)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._login_button_locator).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password)
        return TwoFactorAuthentication(self.selenium)

    def logout(self):
        self.selenium.find_element(*self._avatar_image_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.find_element(*self._logout_button_locator))
        self.selenium.find_element(*self._logout_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(*self._login_button_locator))

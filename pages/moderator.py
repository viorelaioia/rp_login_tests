from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base


class Moderator(Base):
    _login_button_locator = (By.CSS_SELECTOR, 'a[class="login btn btn-primary"]')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href="/oidc/logout/"]')

    def __init__(self, selenium, url):
        super(Moderator, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def login_with_ldap(self, email, password, passcode):
        self.selenium.find_element(*self._login_button_locator).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password, passcode)

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

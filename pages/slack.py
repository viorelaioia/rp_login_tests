from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base
from pages.two_factor_authentication import TwoFactorAuthentication


class Slack(Base):
    _sign_in_button = (By.CSS_SELECTOR, '.btn_info.btn_large')
    _logout_button_locator = (By.ID, 'logout')
    _username_locator = (By.ID, 'team_menu_user_name')

    def __init__(self, selenium, url):
        super(Slack, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_username_displayed(self):
        return self.is_element_visible(*self._username_locator)

    def login_with_ldap(self, email, password):
        self.selenium.find_element(*self._sign_in_button).click()
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password, ldap_only=True)
        return TwoFactorAuthentication(self.selenium)

    def logout(self):
        self.selenium.find_element(*self._username_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

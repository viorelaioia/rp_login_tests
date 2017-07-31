from selenium.webdriver.common.by import By

from pages.auth0 import Auth0
from pages.base import Base


class ServiceNowStage(Base):

    _profile_icon_locator = (By.CSS_SELECTOR, '.sub-avatar')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href*="/logout"]')

    def __init__(self, selenium, url):
        super(ServiceNowStage, self).__init__(selenium)
        self.go_to_url(url)

    @property
    def is_profile_icon_displayed(self):
        return self.is_element_visible(*self._profile_icon_locator)

    def login_with_ldap(self, email, password, passcode):
        auth = Auth0(self.selenium)
        auth.login_with_ldap(email, password, passcode, ldap_only=True)

    def logout(self):
        self.selenium.find_element(*self._profile_icon_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

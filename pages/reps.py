from selenium.webdriver.common.by import By

from pages.base import Base


class Reps(Base):
    _sign_in_button = (By.CSS_SELECTOR, '#login-menu-locator a')
    _logout_button_locator = (By.CSS_SELECTOR, '#logout-menu-locator a[href="/oidc/logout/"]')

    @property
    def is_logout_button_displayed(self):
        return self.is_element_visible(*self._logout_button_locator)

    def click_login_button(self):
        self.selenium.find_element(*self._sign_in_button).click()

    def click_logout(self):
        self.selenium.find_element(*self._logout_button_locator).click()

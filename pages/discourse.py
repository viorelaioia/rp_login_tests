from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import Base


class Discourse(Base):
    _login_button_locator = (By.CSS_SELECTOR, 'button.login-button')
    _avatar_image_locator = (By.CSS_SELECTOR, '#current-user a[class="icon"]')
    _logout_button_locator = (By.CSS_SELECTOR, '.widget-link.logout')

    @property
    def is_avatar_displayed(self):
        return self.is_element_visible(*self._avatar_image_locator)

    def click_login_in_button(self):
        self.selenium.find_element(*self._login_button_locator).click()

    def logout(self):
        self.selenium.find_element(*self._avatar_image_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.find_element(*self._logout_button_locator))
        self.selenium.find_element(*self._logout_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(*self._login_button_locator))

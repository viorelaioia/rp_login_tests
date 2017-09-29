from selenium.webdriver.common.by import By

from pages.base import Base


class Biztera(Base):
    _name_locator = (By.CSS_SELECTOR, 'div[class*="display-name"]')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[bt-sign-out]')

    @property
    def is_name_displayed(self):
        return self.is_element_visible(*self._name_locator)

    def logout(self):
        self.selenium.find_element(*self._name_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

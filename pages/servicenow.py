from selenium.webdriver.common.by import By

from pages.base import Base


class ServiceNow(Base):
    _profile_icon_locator = (By.CSS_SELECTOR, '.sub-avatar')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href*="/logout"]')

    @property
    def is_profile_icon_displayed(self):
        return self.is_element_visible(*self._profile_icon_locator)

    def logout(self):
        self.selenium.find_element(*self._profile_icon_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

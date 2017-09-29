from selenium.webdriver.common.by import By

from pages.base import Base


class MozDataCollective(Base):
    _user_menu_locator = (By.CSS_SELECTOR, '.userMenu')
    _logout_button = (By.CSS_SELECTOR, '.fa-sign-out')

    @property
    def is_user_menu_displayed(self):
        return self.is_element_visible(*self._user_menu_locator)

    def sign_out(self):
        self.selenium.find_element(*self._user_menu_locator).click()
        self.wait_for_element_visible(*self._logout_button)
        self.selenium.find_element(*self._logout_button).click()

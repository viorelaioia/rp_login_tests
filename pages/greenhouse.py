from selenium.webdriver.common.by import By

from pages.base import Base


class Greenhouse(Base):
    _support_link_locator = (By.CSS_SELECTOR, 'li[title="Help!"] a')
    _user_dropdown_menu_locator = (By.CSS_SELECTOR, '.dropdown-toggle')
    _logout_button_locator = (By.CSS_SELECTOR, 'a[href*="logout"]')

    @property
    def is_support_link_displayed(self):
        return self.is_element_visible(*self._support_link_locator)

    def sign_out(self):
        self.selenium.find_element(*self._support_link_locator).click()
        self.selenium.switch_to_window(self.selenium.window_handles[-1])
        self.selenium.find_element(*self._user_dropdown_menu_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

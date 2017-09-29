from selenium.webdriver.common.by import By

from pages.base import Base


class Standups(Base):
    _sign_in_button_locator = (By.CSS_SELECTOR, 'a[href="/accounts/login/"]')
    _sign_in_to_standup_button_locator = (By.CSS_SELECTOR, '.btn.login-button')
    _logout_button_locator = (By.ID, 'logout-link')
    _user_menu_locator = (By.CSS_SELECTOR, '#user-menu img')

    @property
    def is_user_menu_displayed(self):
        return self.is_element_visible(*self._user_menu_locator)

    def click_sign_in(self):
        self.selenium.find_element(*self._sign_in_button_locator).click()
        self.wait_for_element_visible(*self._sign_in_to_standup_button_locator)
        self.selenium.find_element(*self._sign_in_to_standup_button_locator).click()

    def click_logout(self):
        self.selenium.find_element(*self._user_menu_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

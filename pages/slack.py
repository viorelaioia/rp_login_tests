from selenium.webdriver.common.by import By

from pages.base import Base


class Slack(Base):
    _sign_in_button = (By.CSS_SELECTOR, '.btn_info.btn_large')
    _logout_button_locator = (By.ID, 'logout')
    _username_locator = (By.ID, 'team_menu_user_name')

    @property
    def is_username_displayed(self):
        return self.is_element_visible(*self._username_locator)

    def click_sign_in_button(self):
        self.selenium.find_element(*self._sign_in_button).click()

    def logout(self):
        self.selenium.find_element(*self._username_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

from selenium.webdriver.common.by import By

from pages.base import Base


class Smartsheet(Base):
    _avatar_locator = (By.CSS_SELECTOR, '.clsAvatar')
    _logout_button_locator = (By.CSS_SELECTOR, '.clsStandardMenuText span')

    @property
    def is_user_menu_displayed(self):
        return self.is_element_visible(*self._avatar_locator)

    def logout(self):
        self.selenium.find_element(*self._avatar_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

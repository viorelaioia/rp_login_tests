from selenium.webdriver.common.by import By

from pages.base import Base


class Mana(Base):
    _user_menu_locator = (By.CSS_SELECTOR, 'a[id="user-menu-link"]')
    _logout_button_locator = (By.ID, 'logout-link')

    @property
    def is_user_menu_displayed(self):
        return self.is_element_visible(*self._user_menu_locator)

    def logout(self):
        self.selenium.find_element(*self._user_menu_locator).click()
        self.wait_for_element_visible(*self._logout_button_locator)
        self.selenium.find_element(*self._logout_button_locator).click()

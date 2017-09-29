from selenium.webdriver.common.by import By

from pages.base import Base


class SelfServiceMig(Base):
    _user_email_locator = (By.CSS_SELECTOR, '.intro i')

    @property
    def user_email_locator(self):
        return self.selenium.find_element(*self._user_email_locator).text

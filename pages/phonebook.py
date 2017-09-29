from selenium.webdriver.common.by import By

from pages.base import Base


class Phonebook(Base):
    _search_region_locator = (By.ID, 'search-region')

    @property
    def is_search_region_displayed(self):
        return self.is_element_visible(*self._search_region_locator)

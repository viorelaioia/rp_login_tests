import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class Base(object):

    def __init__(self, selenium):
        self.selenium = selenium
        self.timeout = 60

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def is_element_present(self, *locator):
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(10)

    def wait_for_element_visible(self, *locator):
        count = 0
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == self.timeout:
                raise Exception(':'.join(locator) + " is not visible")

    def go_to_url(self, url):
        self.selenium.get(url)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        """ Find a single element using Explicit Wait """
        return WebDriverWait(self.driver, self.timeout).until(
            EC. presence_of_element_located (locator)
        )

    def find_elements(self, locator):
        """ Find multiple elements based on the given locator """
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
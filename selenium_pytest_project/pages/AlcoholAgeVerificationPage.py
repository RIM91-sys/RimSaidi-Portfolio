import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class AlcoholAgeVerificationPage(BasePage):
    SHOP_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/store']")
    DOB_FIELD_LOCATOR = (By.XPATH, "//input[@type='text' and @placeholder='DD-MM-YYYY']")
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Confirm']")
    ALCOHOL_SECTION_LOCATOR = (By.XPATH, "//div[@class='card']//img[@alt='Perlenbacher Pils Alcohol-Free']")
    UNDERAGE_ERROR_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'go3958317564') and contains(text(), 'underage')]")
    ACCESS_GRANTED_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'go3958317564') and contains(text(), 'of age')]")
    ALCOHOL_PRODUCT_BUTTON_LOCATOR = (By.XPATH, "//div[@class='widget widget-menu']//ul/li[10]/a[text()='Alocohol']")


    def __init__(self, driver):
        super().__init__(driver)

    def click_shop(self):
        """Click the 'Shop' button to navigate to the shopping section."""
        self.click(self.SHOP_BUTTON_LOCATOR)

    def enter_dob(self, dob):
        """Enter the date of birth into the DOB input field."""
        self.enter_text(self.DOB_FIELD_LOCATOR, dob)
        time.sleep(2)

    def click_confirm(self):
        """Click the 'Confirm' button to submit the date of birth."""
        self.click(self.CONFIRM_BUTTON_LOCATOR)
        time.sleep(2)

    def age_verification(self, dob):
        """ Complete the age verification process by clicking 'Shop',
            entering a date of birth, and confirming it."""
        self.click_shop()
        self.enter_dob(dob)
        self.click_confirm()

    def alcohol_element_displayed(self):
        """Check whether the alcohol section is visible after age verification.
            Returns:
                bool: True if the alcohol section is displayed, False otherwise.
            """
        try:
            product_alcohol = WebDriverWait(self.driver, self.timeout).until(
                 EC.presence_of_element_located(self.ALCOHOL_SECTION_LOCATOR)
                )
            return product_alcohol.is_displayed()
        except:
            return False

    def get_underage_error_message(self):
        """ Retrieve the error message shown to underage users."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.UNDERAGE_ERROR_MESSAGE_LOCATOR)
        ).text.strip()

    def get_access_granted_message(self):
        """Retrieve the success message shown when access is granted."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.ACCESS_GRANTED_MESSAGE_LOCATOR)
        ).text.strip()

    def click_alcohol_product(self):
        """Click an alcohol product after successful age verification.
            Waits for the product button to be clickable and the section to be visible.
            """
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ALCOHOL_PRODUCT_BUTTON_LOCATOR)
        ).click()
        time.sleep(2)
        # Wait for product list to appear
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.ALCOHOL_SECTION_LOCATOR)
        )
        time.sleep(2)


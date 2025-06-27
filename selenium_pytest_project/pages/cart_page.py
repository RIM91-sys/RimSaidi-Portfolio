# pages/cart_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    # Filters and sorting
    FILTER_5_10 = (By.XPATH, "//div[@class='widget widget-menu']/ul/li/a[text()='5€ - 10€']")
    FILTER_0_5 = (By.XPATH, "//div[@class='widget widget-menu']/ul/li/a[text()='0€ - 5€']")
    SUGGESTED_DROPDOWN = (By.XPATH, "//div[@class='custom-select-container ']/div[@class='custom-select' and normalize-space(text())='Suggested']")
    PRICE_OPTION = (By.XPATH, "//div[@class='custom-options']/div[@class='custom-option' and normalize-space(text())='Price']")

    # Cart elements
    CART_ICON = (By.XPATH, "(//div[@class='headerIcon'])[3]")
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(., 'Checkout')]")
    SHIPPING_COST_CONTAINER = (By.XPATH, "//div[@class='shipment-container']")
    REMOVE_PRODUCT_BUTTONS = (By.XPATH, "//div[@class='checkout-card-image-container']/a")
    SHOP_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/store']")

    PAGE_URL = 'https://grocerymate.masterschool.com/auth'

    def filter_by_price_5_10(self):
        """Apply a price filter to show products priced between €5 and €10."""
        self.click(self.FILTER_5_10)
        time.sleep(2)

    def filter_by_price_0_5(self):
        """Apply a price filter to show products priced between €0 and €5."""
        self.click(self.FILTER_0_5)
        time.sleep(2)

    def sort_by_price(self):
        """Sort the product list by price using the dropdown menu."""
        self.click(self.SUGGESTED_DROPDOWN)
        time.sleep(2)
        self.click(self.PRICE_OPTION)
        time.sleep(2)

    def add_product_by_name(self, product_name):
        """Add a product to the cart by locating it using its name."""
        product_xpath = (By.XPATH, f"//p[@class='lead' and contains(text(), '{product_name}')]/../../..//button[text()='Add to Cart']")
        self.click(product_xpath)

    def open_cart(self):
        """Open the shopping cart view."""
        self.click(self.CART_ICON)
        time.sleep(2)

    def increase_quantity_in_cart(self, times=1):
        """ Increase the quantity of the first item in the cart."""
        plus_button = (By.XPATH, "//div[@class='checkout-quantity']/button[text()='+']")
        for _ in range(times):
            self.click(plus_button)
        time.sleep(2)

    def get_shipping_cost_text(self):
        """Retrieve the shipping cost text displayed in the cart or checkout."""
        element = self.find_element(self.SHIPPING_COST_CONTAINER)
        return element.text

    def clear_cart(self):
        """ Remove all items from the cart.
            Also attempts to return to the product list by clicking the shop button, if available.
            """
        self.open_cart()
        time.sleep(1)
        while True:
            remove_buttons = self.driver.find_elements(By.XPATH, "//div[@class='checkout-card-image-container']/a")
            if not remove_buttons:
                break
            remove_buttons[0].click()
            time.sleep(1)

        # Optional: return to product list if needed
        try:
            self.driver.find_element(*self.SHOP_BUTTON_LOCATOR).click()
        except:
            pass



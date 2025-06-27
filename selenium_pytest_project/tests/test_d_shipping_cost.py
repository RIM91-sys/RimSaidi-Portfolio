# tests/test_d_shipping_cost.py

import pytest
import time
from pages.LoginPage import LoginPage
from pages.cart_page import CartPage
from tests.test_a_login import login_page, test_login_pom
from tests.test_c_alcohol_age_verification import alcohol_page
import utils.constants as constants

@pytest.fixture
def shipping_cost_page(driver):
    driver.get(CartPage.PAGE_URL)
    return CartPage(driver)

@pytest.mark.parametrize("case", [
    {
        "name": "Exactly €20",
        "actions": [("filter_5_10", "Birchwood 2 Welsh Beef Fillet Steaks", 2),
                    ("filter_0_5", "White Crusty Roll", 1)],
        "expected_shipping": "0€"
    },
    {
        "name": "€19.99",
        "actions": [("filter_5_10", "Birchwood 2 Welsh Beef Fillet Steaks", 2)],
        "expected_shipping": "5€"
    },
    {
        "name": "€40",
        "actions": [("filter_5_10", "Birchwood 2 Welsh Beef Fillet Steaks", 4),
                    ("filter_0_5", "White Crusty Roll", 1)],
        "expected_shipping": "0€"
    },
    {
        "name": "€10",
        "actions": [("filter_5_10", "Birchwood 2 Welsh Beef Fillet Steaks", 1),
                    ("filter_0_5", "White Crusty Roll", 1)],
        "expected_shipping": "5€"
    },
    {
        "name": "€15 use case",
        "actions": [("filter_5_10", "Birchwood 2 Welsh Beef Fillet Steaks", 1),
                    ("filter_5_10", "Deluxe Dry Aged Aberdeen Angus Ribeye Steak", 1)],
        "expected_shipping": "5€"
    },
])
def test_shipping_cost_cases(driver, case, login_page, shipping_cost_page, alcohol_page):
    # Login
    time.sleep(2)
    test_login_pom(driver, login_page)
    time.sleep(3)

    # review_page.click_shop()
    # time.sleep(2)
    shipping_cost_page.clear_cart()
    if case.get("dob_required"):
        alcohol_page.enter_dob(constants.VALID_DOB)
    alcohol_page.click_confirm()

    # Perform product additions
    for action in case["actions"]:
        price_filter, product_name, quantity = action
        if price_filter == "filter_5_10":
            shipping_cost_page.filter_by_price_5_10()
        elif price_filter == "filter_0_5":
            shipping_cost_page.filter_by_price_0_5()
            shipping_cost_page.sort_by_price()

        time.sleep(1)
        shipping_cost_page.add_product_by_name(product_name)
        shipping_cost_page.open_cart()
        shipping_cost_page.increase_quantity_in_cart(quantity - 1)  # Already added once
        driver.back()
        time.sleep(1)

    # Open cart and assert shipping cost
    shipping_cost_page.open_cart()
    time.sleep(2)
    shipping_text = shipping_cost_page.get_shipping_cost_text()
    assert case["expected_shipping"] in shipping_text, \
        f"Test '{case['name']}' failed: expected {case['expected_shipping']} in '{shipping_text}'"

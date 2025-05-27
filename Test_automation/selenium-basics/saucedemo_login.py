
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password",
                         [
                             ("standard_user","secret_sauce" ),
                             ("locked_out_user", "secret_sauce"),
                             ("problem_user", "secret_sauce"),
                             ("performance_glitch_user", "secret_sauce"),
                             ("error_user", "secret_sauce"),
                             ("visual_user", "secret_sauce")
                         ])
def test_login_and_verify_product(driver, username, password):
    # Arrange
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Act
    time.sleep(2)
    username_field.send_keys(username)
    time.sleep(2)

    password_field.send_keys(password)
    time.sleep(2)

    login_button.click()

    # Assert
    time.sleep(2)

    products_title = driver.find_element(By.CLASS_NAME, "title")
    time.sleep(2)

    assert "Products" in products_title.text, "Login failed or incorrect page loaded."
    time.sleep(2)

    sauce_labs_backpack = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    assert sauce_labs_backpack.is_displayed(), "'Sauce Labs Backpack' is not displayed on the page."
    sauce_labs_backpack.click()

    driver.quit()



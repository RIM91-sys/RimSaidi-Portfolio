from selenium.webdriver.support.ui import Select
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com")
    driver.maximize_window()
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'fc-cta-consent')]"))
        ).click()
    except:
        pass
    yield driver
    driver.quit()
def test_register_user(driver):
    # 1. Signup / Login
    signup_login_button = driver.find_element(By.XPATH, "//a[@href='/login']")
    signup_login_button.click()

    # 2. Fill New User Signup! (name and email)
    name_field = driver.find_element(By.NAME, "name")
    email_field = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = driver.find_element(By.XPATH, "//button[text()='Signup']")

    name_field.send_keys("Rim")
    email_field.send_keys("Rim.@gmail.com")
    signup_button.click()

    # 3. Fill Account Information
    title_box = driver.find_element(By.ID, "id_gender2")
    password_field = driver.find_element(By.ID, "password")
    Select(driver.find_element(By.ID, "days")).select_by_value("1")
    Select(driver.find_element(By.ID, "months")).select_by_value("5")
    Select(driver.find_element(By.ID, "years")).select_by_value("1990")
    time.sleep(2)
    checkbox1_button = driver.find_element(By.ID, "newsletter")
    checkbox2_button = driver.find_element(By.ID, "optin")

    title_box.click()
    password_field.send_keys("123rim.")
    checkbox1_button.click()
    checkbox2_button.click()

    # 4. Fill Address Information
    time.sleep(2)
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("Rim")

    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("Saidi")

    company_field = driver.find_element(By.ID, "company")
    company_field.send_keys("xxx")


    address1_field = driver.find_element(By.ID, "address1")
    address1_field.send_keys("test1")

    address2_field = driver.find_element(By.ID, "address2")
    address2_field.send_keys("test2")

    Select(driver.find_element(By.ID, "country")).select_by_visible_text("Canada")

    state_field = driver.find_element(By.ID, "state")
    state_field.send_keys("test3")

    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("test4")

    zipcode_field = driver.find_element(By.ID, "zipcode")
    zipcode_field.send_keys("123")

    mobile_number_field = driver.find_element(By.ID, "mobile_number")
    mobile_number_field.send_keys("0123876543")



    # 5. Create account
    time.sleep(2)
    create_account_button= driver.find_element(By.XPATH, "//button[text()='Create Account']")
    create_account_button.click()


    # 6. Continue
    continue_button = driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
    continue_button.click()

    # 7. Verify that 'Logged in as username' is visible
    expected_username = "Rim"
    logged_in_element = driver.find_element(By.XPATH, "//a[contains(., 'Logged in as')]")
    assert logged_in_element.text.strip() == f"Logged in as {expected_username}"

    # 8. Delete account
    delete_button = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
    delete_button.click()

    # 9. Final continue
    final_continue_button = driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
    final_continue_button.click()

    driver.quit()

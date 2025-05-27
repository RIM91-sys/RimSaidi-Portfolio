from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    except TimeoutException:
        pass
    yield driver
    driver.quit()

def test_register_user(driver):
    # 1. Signup / Login
    signup_login_button = driver.find_element(By.XPATH, "//a[@href='/login']")
    signup_login_button.click()

    # 2. Fill New User Signup! (name and email)
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys("Rim")

    email_field = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    email_field.send_keys("Rim2.@gmail.com")

    signup_button = driver.find_element(By.XPATH, "//button[text()='Signup']")
    signup_button.click()

    # 3. Fill Account Information
    title_box = driver.find_element(By.ID, "id_gender2")
    title_box.click()

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("123rim.")

    Select(driver.find_element(By.ID, "days")).select_by_value("1")
    Select(driver.find_element(By.ID, "months")).select_by_value("5")
    Select(driver.find_element(By.ID, "years")).select_by_value("1990")

    checkbox1_button = driver.find_element(By.ID, "newsletter")
    driver.execute_script("arguments[0].click();", checkbox1_button)

    checkbox2_button = driver.find_element(By.ID, "optin")
    driver.execute_script("arguments[0].click();", checkbox2_button)

    # 4. Fill Address Information
    first_name_field = driver.find_element(By.ID, "first_name")
    time.sleep(2)
    first_name_field.send_keys("Rim")

    last_name_field = driver.find_element(By.ID, "last_name")
    time.sleep(2)
    last_name_field.send_keys("Saidi")

    company_field = driver.find_element(By.ID, "company")
    time.sleep(2)
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
    create_account_button= driver.find_element(By.XPATH, "//button[text()='Create Account']")
    time.sleep(2)
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
    #time.sleep(2)

    driver.quit()
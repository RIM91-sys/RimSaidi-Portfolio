import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from pages.LoginPage import LoginPage
import utils.constants as constants

@pytest.fixture
def login_page(driver):
    driver.get(constants.LOGIN_PAGE_URL)
    return LoginPage(driver)


def test_login_pom(driver, login_page):
    time.sleep(2)
    login_page.login(constants.VALID_USERNAME, constants.VALID_PASSWORD)

    # Assert
    logout_link = WebDriverWait(driver,10).until(
         EC.element_to_be_clickable((By.XPATH,"//a[@href='/auth' and text()='Log Out']"))
                                 )
    assert logout_link.is_displayed()

def test_login_invalid(driver, login_page):
    time.sleep(2)
    login_page.login(constants.INVALID_USERNAME, constants.INVALID_PASSWORD)
    assert login_page.get_error_message().lower() == constants.INVALID_USERNAME_OR_PASSWORD_ALERT









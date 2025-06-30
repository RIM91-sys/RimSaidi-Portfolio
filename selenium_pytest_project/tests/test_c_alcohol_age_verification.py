import pytest
import time
from pages.AlcoholAgeVerificationPage import AlcoholAgeVerificationPage
from tests.test_a_login import login_page, test_login_pom
from tests.test_b_review import review_page
import utils.constants as constants


@pytest.fixture
def alcohol_page(driver):
    driver.get(constants.LOGIN_PAGE_URL)
    return AlcoholAgeVerificationPage(driver)

@pytest.mark.parametrize("dob, expected_access_message, expected_error_message", [
    # Boundary value (Legal age assumed 18)
    ("01-01-2006", constants.ACCESS_MESSAGE  , None),      # Underage
    ("01-01-2008", None, constants.UNDERAGE_MESSAGE),      # Just below 18
    # Valid adult
    ("01-01-2000", constants.ACCESS_MESSAGE, None),
    # invalid formats/invalid values
    ("", None, constants.UNDERAGE_MESSAGE),
    ("01-12-2030", None, constants.UNDERAGE_MESSAGE),
    ("10/20/2030", None, constants.UNDERAGE_MESSAGE),
    ("10.20.2003", None, constants.UNDERAGE_MESSAGE),
    ("10202003", None, constants.UNDERAGE_MESSAGE),
])
def test_age_verification(driver, dob, expected_access_message, expected_error_message, login_page, alcohol_page, review_page):
    time.sleep(2)
    test_login_pom(driver, login_page)
    alcohol_page.age_verification(dob)

    if expected_error_message:
        actual_error = alcohol_page.get_underage_error_message()
        assert actual_error == expected_error_message, f"Expected error: '{expected_error_message}', got: '{actual_error}'"
    elif expected_access_message:
        actual_message = alcohol_page.get_access_granted_message()
        assert actual_message == expected_access_message, f"Expected message: '{expected_access_message}', got: '{actual_message}'"

        alcohol_page.click_alcohol_product()
        if not alcohol_page.alcohol_element_displayed():
            driver.save_screenshot("alcohol_section_failure.png")
            assert False, "Alcohol product not displayed after clicking the Alcohol menu."
        # assert alcohol_page.alcohol_element_displayed(), "Alcohol product not displayed after clicking the Alcohol menu."





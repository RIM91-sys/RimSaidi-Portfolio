import pytest
import time
from pages.ReviewPage import ReviewPage
from tests.test_a_login import login_page, test_login_pom
import utils.constants as constants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def review_page(driver):
    driver.get(ReviewPage.PAGE_URL)
    return ReviewPage(driver)

@pytest.mark.parametrize("mode, product, review_text, rating, expected_message", [
    ("available", constants.ORANGES_PRODUCT, None, None, None),    # Test Case:Verify review option availability for purchased product
    ("not_available", constants.GALA_APPLE_PRODUCT, None, None, constants.NEED_TO_BUY_MESSAGE),  # Test Case: Verify review option is not available for non-purchased product
    ("submit", constants.ORANGES_PRODUCT, constants.VALID_REVIEW_TEXT, constants.RATING_STAR, constants.REVIEW_RESTRICTION_MESSAGE),  # Test Case:Verify that user can submit a review for purchased product
])
def test_review_behaviors(driver, review_page, login_page, mode, product, review_text, rating, expected_message):
    test_login_pom(driver, login_page)
    time.sleep(3)

    if mode == "available":
        review_page.review_availability(product)
        review_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@class, 'new-review-form-control') and @placeholder='What is your view?']"))
        )
        assert review_box.is_displayed()

    elif mode == "not_available":
        review_page.review_not_available(product)
        assert review_page.need_to_buy_message() == expected_message

    elif mode == "submit":
        review_page.review_availability(product)
        review_page.submit_review(review_text, rating)
        time.sleep(3)
        assert review_page.review_restriction_message() == expected_message

    else:
        pytest.fail(f"Unsupported test mode: {mode}")

# # Test Case:Verify review option availability for purchased product
# def test_review_option_availability(driver, review_page, login_page):
#
#       test_login_pom(driver, login_page)
#       time.sleep(3)
#
#       review_page.review_availability(constants.ORANGES_PRODUCT)
#
#       review_box= WebDriverWait(driver, 10).until(
#          EC.element_to_be_clickable((By.XPATH, "//textarea[contains(@class, 'new-review-form-control') and @placeholder='What is your view?']")))
#
#       assert review_box.is_displayed()
#
#
# # Test Case: Verify review option is not available for non-purchased product
# def test_review_option_not_available(driver, review_page, login_page ):
#     test_login_pom(driver, login_page)
#     time.sleep(3)
#
#     review_page.review_not_available(constants.GALA_APPLE_PRODUCT)
#     assert review_page.need_to_buy_message() == constants.NEED_TO_BUY_MESSAGE
#
# # Test Case:Verify that user can submit a review for purchased product
# def test_valid_review(driver, review_page, login_page):
#     test_login_pom(driver, login_page)
#     time.sleep(3)
#
#     # Arrange
#     review_page.review_availability(constants.ORANGES_PRODUCT)
#     review_page.submit_review(constants.VALID_REVIEW_TEXT, constants.RATING_STAR)
#     time.sleep(3)
#     assert review_page.review_restriction_message() == constants.REVIEW_RESTRICTION_MESSAGE


@pytest.mark.parametrize(
    "comment, rating, expected_error, expected_rating_display, expected_comment_display",
    [
        ("a" * 499, 3, None, '***' , ""),  # BVA 499
        ("a" * 500, 3, "You cannot tell us more about this product.", '***', None),  # BVA 500
        ("a" * 501, 3, "You cannot tell us more about this product.", '***', None),  # BVA 501
        (" ", 3, None, "***", ""),  # EP Whitespace only
        ("great taste!", None, "Invalid input for the field 'Rating'. Please check your input.", None, None) #Error guessing
    ]
)

def test_1_review_submissions(driver, review_page, login_page,  comment, rating, expected_error, expected_rating_display, expected_comment_display):
    time.sleep(3)
    test_login_pom(driver, login_page)

    # Clear any existing review before starting the test
    review_page.review_availability(constants.ORANGES_PRODUCT)
    time.sleep(2)

    if review_page.review_exists():
        review_page.click_delete_review()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(2)  # Give time for UI to update after deletion

    # Submit new review
    review_page.submit_review(comment, rating)

    if expected_error:
        if rating is None:
            # Error for missing rating comes after click
            assert expected_error in review_page.input_error_message()
        else:
            # Error for invalid text length appears before/after click depending on frontend behavior
            assert expected_error in review_page.get_error_message()

    else:
        if expected_rating_display:
            # assert review_page.get_displayed_star_rating() == expected_rating_display
            displayed_rating = review_page.get_displayed_star_rating()
            assert displayed_rating == expected_rating_display, f"Expected rating {expected_rating_display}, but got {displayed_rating}"
        if expected_comment_display is not None:
            assert expected_comment_display in review_page.get_existing_comment()


# EP : Delete an existing product review
def test_2_delete_existing_review(driver, review_page, login_page):
    # Step 1: Log in
    test_login_pom(driver, login_page)

    # Step 2: Ensure a review exists (submit one if not present)
    review_page.review_availability(constants.ORANGES_PRODUCT)
    time.sleep(2)
    if not review_page.review_exists():
        review_page.submit_review(constants.VALID_REVIEW_TEXT, constants.RATING_STAR)
        time.sleep(2)

    # Step 3: Delete the existing review
    review_page.click_delete_review()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(3)  # Wait for UI update

    # Step 4: Assert the review is gone and review textbox is available
    assert not review_page.review_exists(), "Review still exists after deletion."
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(review_page.REVIEW_TEXTBOX_LOCATOR)
    )


# Error Guessing: Submit multiple reviews for the same product by the same user.
def test_3_submit_multiple_reviews(driver, review_page, login_page):
    time.sleep(3)
    test_login_pom(driver, login_page)

    # Clear any existing review before starting the test
    review_page.review_availability(constants.ORANGES_PRODUCT)
    time.sleep(3)
    if review_page.review_exists():
        review_page.click_delete_review()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(3)  # Give time for UI to update after deletion

    # Submit new review
    review_page.submit_review(constants.VALID_REVIEW_TEXT, constants.RATING_STAR)
    # Assert the review restriction message is shown
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(review_page.REVIEW_RESTRICTION_MESSAGE_LOCATOR)
    )
    restriction_text = review_page.review_restriction_message()
    assert "You have already reviewed this product." in restriction_text


@pytest.mark.parametrize("initial_rating, new_rating, comment, expected_comment, expected_rating", [
    (5, 2, "", "", '**'),     # Equivalence Partitioning: Edit rating only, no comment
    (4, 0, "", None, '****'),  # Error Guessing: Attempt 0-star edit (we simulate this by not allowing 0 to be set) # Expect no change if 0-star is ignored
    (5, 5, "good quality", "good quality", '*****'),     # Error Guessing: Add comment to existing review
    (5, 4, "good quality", "good quality", '****'),     # Edit rating and Add comment
    (5, 5, "Great taste! #Delicious", "Great taste! #Delicious", '*****')     # Equivalence Partitioning: Special characters
])

def test_4_edit_review(driver, review_page, login_page, initial_rating, new_rating, comment, expected_comment, expected_rating):
    time.sleep(3)
    test_login_pom(driver, login_page)

    # Ensure review section is accessible
    review_page.review_availability(constants.ORANGES_PRODUCT)
    time.sleep(2)

    # Clear existing review (if any)
    if review_page.review_exists():
        review_page.click_delete_review()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        time.sleep(2)

    # Submit a review with the initial state
    review_page.submit_review(expected_comment if expected_comment else constants.VALID_REVIEW_TEXT, initial_rating)

    # Perform edit
    review_page.edit_review(new_rating, comment)
    time.sleep(2)  # Allow UI to update

    # Validate rating
    displayed_rating = review_page.get_displayed_star_rating()
    assert displayed_rating == expected_rating, f"Expected rating {expected_rating}, but got {displayed_rating}"

    # Validate comment
    displayed_comment = review_page.get_existing_comment()
    expected_display_comment = expected_comment or ""
    assert displayed_comment == expected_display_comment, f"Expected comment '{expected_display_comment}', but got '{displayed_comment}'"






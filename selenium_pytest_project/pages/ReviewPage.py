import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ReviewPage(BasePage):
      DOB_FIELD_LOCATOR = (By.XPATH, "//input[@type='text' and @placeholder ='DD-MM-YYYY' ]")
      CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Confirm']")
      # PRODUCT_ORANGE_LOCATOR = (By.XPATH, "//img[@alt='Oranges']")
      SEARCH_BUTTON_LOCATOR = (By.XPATH, "//input[@placeholder='Search Products']")
      ORANGES_BUTTON_SEARCH_LOCATOR = (By.XPATH, "//div[@class='suggestion-item']/p[strong[text()='Oranges']]")
      GALA_APPLE_BUTTON_SEARCH_LOCATOR = (By.XPATH, "//div[@class='suggestion-item']/p[strong[text()='Gala Apples']]")
      REVIEW_TEXTBOX_LOCATOR = (By.XPATH, "//textarea[contains(@class, 'new-review-form-control') and @placeholder='What is your view?']")
      RATING_STARS_LOCATOR = (By.XPATH, '//div[@class="interactive-rating"]/span[contains(@class, "star") and contains(@class, "empty")]')
      SEND_REVIEW_BUTTON_LOCATOR = (By.XPATH, "//button[@class='new-review-btn new-review-btn-send']")
      REVIEW_RESTRICTION_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'reviewRestriction')]/p")
      NEED_TO_BUY_MESSAGE_LOCATOR = (By.XPATH, "//div[@class='reviewRestriction']/p[text()='You need to buy this product to tell us your opinion!']")
      INVALID_INPUT_MESSAGE_LOCATOR = (By.XPATH, "//div[@role='status' and contains(., \"Invalid input for the field 'Rating'.\")]") #class="go3958317564">Invalid
      ERROR_MESSAGE_LOCATOR = (By.XPATH, "//p[@class='error-message' and text()='You cannot tell us more about this product.']")
      EXISTING_COMMENT_LOCATOR = (By.XPATH, "(//div[@class = 'comment-header'])[1]/following-sibling::p")
      EXISTING_RATING_LOCATOR = (By.XPATH,'(//div[@class = "rating"])[1]/span[@class = "small"]')
      ICON_BUTTON_LOCATOR = (By.XPATH, "//section[@class='product-comments']//div[@class='comment']//div[@class='comment-header']//div[@class='menu-icon']")
      DELETE_REVIEW_BUTTON = (By.XPATH, "//div[@class='dropdown-menu']//button[text()='Delete']")
      EDIT_REVIEW_BUTTON = (By.XPATH, "//div[@class='dropdown-menu']//button[text()='Edit']")
      REVIEW_NAME_LOCATOR = (By.XPATH, "//div[@class= 'comment-header']//strong[text()= 'Rym']")
      SAVE_CHANGES_BUTTON = (By.XPATH, "//div[@class='modal-buttons']//button[text()='Save Changes']")
      RATING_DROPDOWN_LOCATOR = (By.XPATH, "//label[contains(., 'Rating')]/input[@type='number']")
      COMMENT_TEXTAREA_LOCATOR = (By.XPATH, "//label[contains(., 'Comment')]/textarea")
      UNDERAGE_ERROR_MESSAGE_LOCATOR = (By.XPATH, "//div[@class='go3958317564' and contains(text(), 'You are underage')]")
      ACCESS_GRANTED_MESSAGE_LOCATOR = (By.XPATH, "//div[@class='go3958317564' and contains(text(), 'You are of age')]")


      PAGE_URL = 'https://grocerymate.masterschool.com/auth'

      def __init__(self, driver):
          super().__init__(driver)

      def search_product(self, search_product):
          """Enter a product name in the search input field."""
          self.enter_text(self.SEARCH_BUTTON_LOCATOR, search_product)

      def click_oranges(self):
          """Click on the oranges button from the search results."""
          self.click(self.ORANGES_BUTTON_SEARCH_LOCATOR)

      def review_availability(self, search_product):
          """Search for a product and click the oranges result."""
          self.search_product(search_product)
          self.click_oranges()

      def click_gala_apple(self):
          """Click on the Gala Apple button from the search results."""
          self.click(self.GALA_APPLE_BUTTON_SEARCH_LOCATOR)

      def review_not_available(self, search_product):
          """Search for a product and click the Gala Apple result."""
          self.search_product(search_product)
          self.click_gala_apple()

      def need_to_buy_message(self):
          """Retrieve the 'Need to Buy' message from the page."""
          time.sleep(3)
          element = self.find_element(self.NEED_TO_BUY_MESSAGE_LOCATOR)
          return element.text

      def add_comment(self,comment):
          """Enter a comment into the review textbox."""
          self.enter_text(self.REVIEW_TEXTBOX_LOCATOR, comment)

      def select_rating(self, rating):
          """Select a star rating based on the given value."""
          elements = self.find_elements(self.RATING_STARS_LOCATOR)
          if 1 <= rating <= len(elements):
              elements[rating - 1].click()
          time.sleep(3)

      def click_send(self):
          """Click the 'Send Review' button to submit the review."""
          self.click(self.SEND_REVIEW_BUTTON_LOCATOR)

      def submit_review(self, comment, rating):
          """Submit a product review with comment and rating."""
          self.add_comment(comment)

          # Only attempt to select rating if it's provided
          if rating is not None:
              try:
                  self.select_rating(rating)
              except TimeoutException:
                  print("Rating stars not found or not interactable.")
          self.click_send()

      def click_delete_review(self):
          """Delete an existing review by clicking the delete button."""
          self.click(self.ICON_BUTTON_LOCATOR)
          time.sleep(2)
          self.click(self.DELETE_REVIEW_BUTTON)

      def input_error_message(self):
          """Retrieve the error message displayed for invalid input."""
          return WebDriverWait(self.driver, self.timeout).until(
                  EC.visibility_of_element_located(self.INVALID_INPUT_MESSAGE_LOCATOR)).text

      def get_error_message(self):
          """Retrieve and handle a specific error message displayed on the page."""
          return WebDriverWait(self.driver, self.timeout).until(
                  EC.visibility_of_element_located(self.ERROR_MESSAGE_LOCATOR)).text

      def get_displayed_star_rating(self):
          """Retrieve the displayed star rating as a string of asterisks.
              Returns:
                  str: The rating as asterisks (e.g., "***"), or an empty string if not found.
              """
          try:
              rating_element = self.driver.find_element(*self.EXISTING_RATING_LOCATOR)
              #print (rating_element)
              text = rating_element.text.strip("()")
              return int(text) * '*'
          except Exception as e:
              print(f"Error getting rating: {e}")
              return ""

      # def get_displayed_star_rating(self):
      #     try:
      #         # Get only the first rating container
      #         rating_container = self.driver.find_element(By.XPATH, '(//div[@class="rating"])[1]')
      #         full_stars = rating_container.find_elements(By.CSS_SELECTOR, ".custom-rating .star.full")
      #         return len(full_stars) * '*'
      #     except Exception as e:
      #         print(f"Error getting visual stars: {e}")
      #         return ""

      def get_existing_comment(self):
          """Get the existing review comment text."""
          return self.find_element(self.EXISTING_COMMENT_LOCATOR).text

      def review_exists(self):
          """Check if a review currently exists on the page.
              Returns:
                  bool: True if the review is displayed, False otherwise.
              """
          try:
              # Option 1: check if comment or rating is displayed
              review_name = self.driver.find_element(*self.REVIEW_NAME_LOCATOR)
              return review_name.is_displayed()
          except NoSuchElementException:
              return False

      def review_restriction_message(self):
          """Get the message displayed when review submission is restricted."""
          element = self.find_element(self.REVIEW_RESTRICTION_MESSAGE_LOCATOR)
          return element.text

      def click_edit_review(self):
          """Click to open the edit review modal."""
          self.click(self.ICON_BUTTON_LOCATOR)
          self.click(self.EDIT_REVIEW_BUTTON)

      def click_save_changes(self):
          """Click the button to save changes after editing a review."""
          self.click(self.SAVE_CHANGES_BUTTON)

      def edit_review(self, rating, comment):
          """Edit an existing review with new rating and/or comment."""
          self.click_edit_review()

          # Wait for modal to appear
          WebDriverWait(self.driver, 5).until(
              EC.presence_of_element_located((By.CLASS_NAME, "modal"))
          )

          # Rating input (if valid)
          if 1 <= rating <= 5:
              rating_input = self.driver.find_element(*self.RATING_DROPDOWN_LOCATOR)
              rating_input.clear()
              rating_input.send_keys(str(rating))
          time.sleep(2)

          # Comment textarea
          comment_box = self.driver.find_element(*self.COMMENT_TEXTAREA_LOCATOR)
          comment_box.clear()
          if comment:
              comment_box.send_keys(comment)
          time.sleep(2)

          # Save changes
          self.click_save_changes()

          # Optional: wait until modal disappears
          WebDriverWait(self.driver, 10).until(
              EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
          )

          time.sleep(2)

      def click_comment_box(self):
          """Click the comment textbox to focus on it."""
          self.click(self.REVIEW_TEXTBOX_LOCATOR)

























      # def submit_update_review(self, comment, rating):
      #     # Wait for modal to be visible
      #     WebDriverWait(self.driver, 10).until(
      #         EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal"))
      #     )
      #
      #     # Fill rating (input type="number")
      #     rating_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='number']")
      #     rating_input.clear()
      #     rating_input.send_keys(str(rating))
      #
      #     # Fill comment
      #     comment_box = self.driver.find_element(By.CSS_SELECTOR, "textarea")
      #     comment_box.clear()
      #     comment_box.send_keys(comment)
      #
      #     # Click save button
      #     save_button = self.driver.find_element(By.XPATH,
      #                                            "//div[@class='modal-buttons']//button[normalize-space()='Save Changes']")
      #     save_button.click()





      def get_review_message(self):
          return self.find_element(self.REVIEW_TEXTBOX_LOCATOR).text
















Here's the test execution documentation adapted for the GroceryMate website and the three tested features: **Product Rating and Reviews**, **Age Verification for Alcohol Category**, and **Shipping Cost Changes**.
# GroceryMate - Test Execution Report

## Feature 1: Product Rating and Reviews
### Scenario 1: Product Review – Purchase Required

As a user, I can only leave a review for a product after I have purchased it.


| Step# | Action                                               | Expected Outcome                                                                 | OK/NOK | URL                                        | Link to issue |
|-------|------------------------------------------------------|----------------------------------------------------------------------------------|--------|--------------------------------------------|----------------|
| 1     | Log in to GroceryMate                                | User is successfully logged in                                                   | OK     | https://grocerymate.masterschool.com/      |                |
| 2     | Click “Shop” and browse categories                   | Product listing appears                                                          | OK     | /store                                     |                |
| 3     | Click on "Fresh Vegetables" category                 | Category page loads                                                              | OK     | /store#                                    |                |
| 4     | Click on product “Braeburn Apples”                   | Product detail page opens                                                        | OK     | /product/66b3a57b3fd5048eacb4798f          |                |
| 5     | Scroll to the review section                         | Message shown: “You need to buy this product to tell us your opinion!”           | OK     | /product/66b3a57b3fd5048eacb4798f          |                |
| 6     | Attempt to leave a review without purchasing         | System blocks input field / review button                                        | OK     |                                            |                |

<img width="1044" alt="Screenshot 2025-05-13 at 13 19 29" src="https://github.com/user-attachments/assets/b46d8e27-d02b-4f23-8eec-1f69f093afe5" />

### Scenario 2: Add Product Review (Valid Input)

| Step# | Action                                            | Expected outcome                | OK/NOK | URL                                                | Link to issue |
| ----- | ------------------------------------------------- | ------------------------------- | ------ | ---------------------------------------------------| ------------- |
| 1     | Log in to GroceryMate                             | User is successfully logged in  | OK     | https://grocerymate.masterschool.com/              |               |
| 2     | Navigate to any purchased product                 | Product page loads              | OK     | /store                                             |               |
| 3     | Scroll to reviews section                         | Review input is visible         | OK     |                                                    |               |
| 4a    | Rate product (e.g. 4 stars)                       | Stars are selected              | OK     |                                                    |               |
| 4b    | Enter review text: "Great taste, will buy again!" | Text input accepted             | OK     |                                                    |               |
| 5     | Click “Send”                             |Review with stars only is accepted and displayed, so I expect that when a text comment is also provided, the review should display both the rating and the comment  | NOK     |                                                    |               |
<img width="1176" alt="Screenshot 2025-05-16 at 01 41 31" src="https://github.com/user-attachments/assets/8bb0759f-06a8-427f-b856-25c65848b7de" />
<img width="1268" alt="Screenshot 2025-05-16 at 01 41 42" src="https://github.com/user-attachments/assets/7e77e960-3b28-48dd-b389-7c3e76f914fd" />

### Scenario 3: Edit Existing Product Review to Add Comment (Error Guessing)

| Step# | Action                                                        | Expected outcome                                                        | OK/NOK | URL                                                                            | Link to issue |
| ----- | ------------------------------------------------------------- | ----------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------ | ------------- |
| 1     | Log in to GroceryMate                                         | User is successfully logged in                                          | OK     | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Navigate to a previously reviewed product                     | Product page with existing review loads                                 | OK     | /store/product/123                                                             |               |
| 3     | Scroll to reviews section                                     | Existing review is visible with 5-star rating                           | OK     |                                                                                |               |
| 4     | Click “Edit” on the existing review                           | Review text box and star rating are now editable                        | OK     |                                                                                |               |
| 5     | Add comment: "Great taste, will buy again!" and retain existing 4-star rating | Text field accepts new input, star selection remains                    | OK     |                                                                                |               |
| 6     | Click “Save Changes”                                                  | Review now displays: 5-star rating and comment: "Good quality"          | OK     |                                                                                |               |
| 7     | Refresh the page to validate persistence                      | Edited review still displays both the 5-star rating and the new comment | OK     |                                                                                |               |
| 8     | Check for duplicate or overwritten data                       | Only one review appears; updated correctly                              | OK     |                                                                                |               |

<img width="1470" alt="Screenshot 2025-05-16 at 01 42 04" src="https://github.com/user-attachments/assets/d710b81e-e13e-472a-a88d-f80b5d2e11ea" />

<img width="1285" alt="Screenshot 2025-05-16 at 01 42 27" src="https://github.com/user-attachments/assets/859173a2-3a6c-4830-8902-ea71d81e1df4" />


### Scenario 4: Post Review with Empty Text
Users should be able to submit a rating without writing a comment. Review text is optional (max 200 characters).

| Step# | Action                                                                  | Expected Outcome                                       | OK/NOK | URL                                               | Link to issue |
|-------|-------------------------------------------------------------------------|--------------------------------------------------------|--------|---------------------------------------------------|----------------|
| 1     | Go to https://grocerymate.masterschool.com/                             | Homepage loads                                         | OK     | https://grocerymate.masterschool.com/             |                |
| 2     | Log in as a registered user who previously purchased a product          | Login successful                                       | OK     | /auth                                             |                |
| 3     | Navigate to the purchased product page (e.g., “Braeburn Apples”)        | Product detail page displays                           | OK     | /product/66b3a57b3fd5048eacb47999                 |                |
| 4     | Scroll to “Reviews” section                                             | Review panel is visible                                | OK     | Product detail page                               |                |
| 5     | Select 4 stars without typing any text                                  | Star selection registered/ Stars highlighted           | OK     |                                                   |                |
| 6     | Leave the text area empty  and Click “Send”                    | Review with stars only is accepted and displayed       | OK     |                                                   |                |

## Feature 2: Age Verification for Alcohol Category

### Scenario 1: Age Verification - Underage User Blocked from Alcohol

A user under 18 cannot access alcohol product pages.
| Step# | Action                                   | Expected outcome                                   | OK/NOK | URL                                  | Link to issue |
| ----- | ---------------------------------------- | ---------------------------------------------------| ------ | -----------------                    | ------------- |
| 1     | Log in to GroceryMate                    | User is successfully logged in                     | OK     | https://grocerymate.masterschool.com/|               |
| 2     | Click “Shop”                             | Age check appears                                  | OK     | /store                               |                |
| 3     | Enter birthdate: 2008-01-01 (user is 17) | Submission accepted and a message appear: You are underage. You can still browse the site, but you will not be able to view alcohol products. | OK     |                   |               |                  
| 4     | Navigate to alcohol category             | Access denied with error: Sorry no products founds! Underage Notice             | NOK     | store#|               |

<img width="1456" alt="Screenshot 2025-05-13 at 13 41 14" src="https://github.com/user-attachments/assets/641a1753-5bbc-4ebb-99e9-218186693ebb" />

<img width="1029" alt="Screenshot 2025-05-13 at 14 30 46" src="https://github.com/user-attachments/assets/ebb5f691-2369-4b75-b452-45153de3bba6" />

<img width="1368" alt="Screenshot 2025-05-13 at 13 41 37" src="https://github.com/user-attachments/assets/6b4949b1-ec7b-47b0-8ff0-c5433b4f7216" />

<img width="1439" alt="Screenshot 2025-05-13 at 13 42 51" src="https://github.com/user-attachments/assets/cfd8dab2-8440-43dc-b2ba-691394021873" />


### Scenario 2: Age Verification - Adult User Gets Access

A user 18 years or older can access alcohol product pages
| Step# | Action                                   | Expected outcome                         | OK/NOK | URL               | Link to issue |
| ----- | ---------------------------------------- | ---------------------------------------- | ------ | ----------------- | ------------- |
| 1     | Log in to GroceryMate                    | User is successfully logged in           | OK     | https://grocerymate.masterschool.com/|               |
| 2     | Click “Shop”                             | Age check appears                        | OK     | /store                               |                |
| 3     | Enter birthdate: 2007-01-01 (user is 18) | Submission accepted and a message appear: You are of age. You can now view all products, even alcohol products. | OK     |                   |               |                  
| 4     | Navigate to alcohol category             | User is granted access to alcohol products             | OK     | /store#|               |

<img width="1030" alt="Screenshot 2025-05-13 at 13 51 55" src="https://github.com/user-attachments/assets/077727fb-4d7d-4338-96d8-c9690977cbd8" />
<img width="1438" alt="Screenshot 2025-05-13 at 13 52 13" src="https://github.com/user-attachments/assets/6fb93598-b90f-46d6-a61e-3c6c5e031c35" />
<img width="1447" alt="Screenshot 2025-05-13 at 13 53 22" src="https://github.com/user-attachments/assets/f2bb929d-2af4-4582-9828-7ae32e913cf9" />

### Scenario 3: Age Verification - User Input Invalid Age Value

| Step# | Action                                   | Expected Outcome                                       | OK/NOK | URL                                       | Link to issue |
|-------|------------------------------------------|--------------------------------------------------------|--------|-------------------------------------------|----------------|
| 1     | Log in to GroceryMate                    | User is successfully logged in                     | OK     | https://grocerymate.masterschool.com/|               |
| 2     | Click “Shop”                             | Age check appears                                  | OK     | /store                               |                |
| 3     | Leave date field empty and click Confirm | Submission accepted and a message appear: You are underage. You can still browse the site, but you will not be able to view alcohol products. | OK     |                   |               |                  
| 4     | Navigate to alcohol category             | Access denied with error: Sorry no products founds! Underage Notice             | OK     | store#|               |

<img width="1456" alt="Screenshot 2025-05-13 at 13 41 14" src="https://github.com/user-attachments/assets/b9e142a8-2738-43c6-87b6-54f9039762dc" />
<img width="1368" alt="Screenshot 2025-05-13 at 13 41 37" src="https://github.com/user-attachments/assets/b4594688-ad43-4c83-b928-29db1794384a" />
<img width="1439" alt="Screenshot 2025-05-13 at 13 42 51" src="https://github.com/user-attachments/assets/e51ff273-a2d5-4f28-a268-785b9f8b698b" />

## Feature 3: Shipping Cost Changes

### Scenario 1: Shipping Cost – Below Free Shipping Threshold

When cart total is below €20, a shipping fee is applied.
| Step# | Action                      | Expected outcome            | OK/NOK | URL       | Link to issue |
| ----- | --------------------------- | --------------------------- | ------ | --------- | ------------- |
| 1     | Log in to GroceryMate                    | User is successfully logged in           | OK     | https://grocerymate.masterschool.com/|               |
| 2     | Click “Shop”                             | Age check appears                        | OK     | /store                               |                |
| 3     | Enter birthdate: 2007-01-01 (user is 18) | Submission accepted  | OK     |                   |               |                  
| 4     | Add items worth €19,99 or less to cart | Items added                 | OK     | /checkout    |               |
| 5     | Proceed to checkout         | Checkout page loads         | OK     | /checkout |               |
| 6     | View shipping cost          | €5 shipping fee is shown | OK     |           |               |
<img width="1302" alt="Screenshot 2025-05-13 at 16 13 25" src="https://github.com/user-attachments/assets/ddd34930-e4d4-4cf5-8902-d6a86440319f" />

### Scenario 2: Shipping Cost – Above Free Shipping Threshold

When cart total is €20 or more, shipping is free.
| Step# | Action                      | Expected outcome      | OK/NOK | URL       | Link to issue |
| ----- | --------------------------- | --------------------- | ------ | --------- | ------------- |
| 1     | Log in to GroceryMate                    | User is successfully logged in           | OK     | https://grocerymate.masterschool.com/|               |
| 2     | Click “Shop”                             | Age check appears                        | OK     | /store                               |                |
| 3     | Enter birthdate: 2007-01-01 (user is 18) | Submission accepted  | OK     |                   |               |                  
| 4     | Add items worth €20 or more to cart | Items added                 | OK     | /checkout     |               |
| 5     | Proceed to checkout         | Checkout page loads         | OK     | /checkout |               |
| 6     | Check shipping fee          | Shipping = Free       | OK     |           |               |
<img width="1264" alt="Screenshot 2025-05-13 at 16 14 25" src="https://github.com/user-attachments/assets/ba579f35-0c3e-4356-8029-1d6b7aa8a79c" />

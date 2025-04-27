 ## **The software**

- MarketMate Webshop, with the following existing functionalities:
- Register and login functionality
- Search for products, sort by price, browse by categories
- Add products to favorites
- Add products to basket
- Checkout process: billing and shipping form, choosing payment method, calculating total price

## **New features**
### **1. Product Rating System**
**Vague Requirement**:

-Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions**:

1. Is it possible for a user to modify or remove their rating and review after submitting it?
2. Are there any guidelines or limitations for the reviews? (such as profanity checks, maximum character count, etc.)
3. Is writing a review required, or can users submit only a star rating without additional comments?
4. Where will the user ratings and reviews appear (directly on the product page, under a separate "Reviews" section)?
5. Can a user submit multiple ratings for the same product?

**Detailed Requirement**:
-Users should be able to select 1 to 5 stars when rating a product. Optionally, they can leave a written review (up to 200 characters). Users can edit or delete their review later through their account. Reviews and ratings will be displayed on each product’s page under a "Reviews" section. Profanity will be automatically filtered out.

### **2. Age Verification for Alcoholic Products**

**Vague Requirement**:
-Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions**:

1. What should happen if a user enters an age below 18? (e.g., block access, redirect to homepage?)
2. Should the age be stored anywhere, or should users re-enter it every time they visit the alcohol section?
3. How strict should the verification be — is entering an age enough, or should it require document upload in the future?
4. What happens if a user inputs an invalid value (e.g., letters instead of numbers)?

**Detailed Requirement**:
-When a user tries to access the "Alcohol" category, a pop-up modal appears asking for their date of birth. If the user is under 18, they are redirected back to the homepage with a message stating they cannot view alcoholic products. Users who are 18+ can continue to browse normally. No personal data is saved from this modal at this stage.

### **3. Shipping Cost Changes**
**Vague Requirement**:
-Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions**:

1. What is the specific minimum amount required to qualify for free shipping?
2. Where should the shipping cost (or free shipping) be displayed — in the cart, during checkout, or both?
3. Should applying promotional codes or discounts impact the eligibility for free shipping?

**Detailed Requirement**:
-Free shipping applies to orders totaling €50 or more (after discounts are applied). Orders below €50 will incur a €4 shipping fee. Shipping costs will be shown in the shopping cart and confirmed again on the checkout page. Only domestic orders qualify for this free shipping offer.



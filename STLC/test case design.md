**Design your test cases based on the features that will be developed for the upcoming release of the online grocery shop!**

**You only have to design them, the execution will happen in a later phase.**

**Add the test design technique, if applicable.**


### **1. Product Rating and Reviews**

**Test Design Techniques**: Use Case Testing,  Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:
1. **Use Case Testing**:
       - **Test Case**:Verify review option availability.
         - **Input**: User visits a product page without having purchased the product.
         - **Expected Outcome**: Review submission is disabled. Message displayed: "You need to buy this product to tell us your opinion!"
2. **Use Case Testing**:
      - **Test Case**: Verify review option availability for purchased product.
         - **Input**: User visits a product page after purchasing the product.
         - **Expected Outcome**: Review submission is enabled. Message displayed: "Add a comment"
3. **Boundary Value Analysis**:
    - **Test Case**: Verify submission of a review with exactly 500 characters.
        - **Input**: Review text = 500 characters, Rating = 5 stars.
        - **Expected Outcome**: review not submitted error message :"You cannot tell us more about this product."
4. **Boundary Value Analysis**:
    - **Test Case**: Verify submission of a review with exactly 499 characters.
        - **Input**: Review text = 499 characters, Rating = 5 stars.
        - **Expected Outcome**: Review is saved successfully. On the product page, only the star rating is displayed, and the comment section is hidden.
5. **Boundary Value Analysis**:
    - **Test Case**: Verify submission of a review when review exceeds 500 characters.
        - **Input**: Review text = 501 characters, Rating = 4 stars.
        - **Expected Outcome**: Error message: "You cannot tell us more about this product"
6. **Equivalence Partitioning**:        
    - **Test Case**: Edit a rating-only review without adding a comment.
        - **Input**: Edit an existing review by changing the star rating (e.g., from 5 stars to 2 stars), leave the comment field empty, and click "Save Changes".
        - **Expected Outcome**: The new star rating is saved and updated correctly. On the product page, the updated rating is displayed, and no comment is shown.
7. **Equivalence Partitioning**: 
    - **Test Case**: Submit a review with special characters and emojis.
        - **Input**: Review text = "Great taste! 😋👍 #Delicious"; Rating = 5 stars.
        - **Expected Outcome**: Review submitted successfully and special characters/emojis are rendered correctly.
8. **Equivalence Partitioning**:
    - **Test Case**: Submit a review with only whitespace characters.
        - **Input**: Review text = "   "; Rating = 3 stars.
        - **Expected Outcome**: Review submitted successfully and Rating shown under product reviews.
9. **Error Guessing**:
    - **Test Case**: Attempt to submit a review without selecting a rating.
        - **Input**: Review text = "Not Satisfied"; Rating = not selected.
        - **Expected Outcome**: Error message displayed: "Invalid input for the field 'Rating! Please check your input." The review is not saved or displayed.
10. **Error Guessing**:
     - **Test Case**: Verify that user cannot edit a review to select a 0-star rating.
        - **Input**: Attempt to edit an existing review (with 1–5 stars) and change the rating to 0 stars.
        - **Expected Outcome**: The 0-star option is not available in the rating selection. User cannot choose a rating below 1 star. Existing rating remains unchanged unless a valid (1–5 stars) rating is selected.      
11. **Error Guessing**: 
     - **Test Case**: Edit existing review to add a comment
        - **Input**: Edit the previously submitted 5-star review, add comment = "Good quality", and submit.
        - **Expected Outcome**: Comment is now visible under the product review, along with the rating.
12. **Error Guessing**:
     - **Test Case**: Submit multiple reviews for the same product by the same user.
        - **Input**: Submit two reviews for the same product.
        - **Expected Outcome**: Second submission is either prevented with a message: "You have already reviewed this product." Only the first review appears on the product page.

       
### **2. Age Verification for Alcohol Category**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Access Alcohol category for a user exactly 18 years old.
        - **Input**: Date of Birth = (Today’s date - 18 years)
        - **Expected Outcome: User is granted access to the Alcohol category.
2. **Boundary Value Analysis**:
    - **Test Case**: Access Alcohol category for a user just below 18 years.
        - **Input**: Date of Birth = (Today’s date- 18 years + 1 day)
        - **Expected Outcome**: Access denied, user redirected to homepage with a restriction message.
3. **Equivalence Partitioning**:
    - **Test Case**: Access Alcohol category for users below the age of 18.
        - **Input**: Date of Birth = (Today’s date - 17 years)
        - **Expected Outcome**: Access denied and redirected.
3. **Equivalence Partitioning**:
    - **Test Case**: Access Alcohol category for users above the age of 18.
        - **Input**:  Date of Birth = (Today’s date - 25 years)
        - **Expected Outcome**: Access granted.
4. **Error Guessing**:
    - **Test Case**: Verify system behavior when Date of Birth is not entered.
        - **Input**: Date of Birth field left empty.
        - **Expected Outcome**: Error message "You are underage. You can still browse the site, but you will not be able to view alcohol products."
5. **Error Guessing**:
    - **Test Case**: Verify system behavior when a date of birth is entered in an invalid format or contains invalid values.
        - **Input**: Date of Birth = "01-12-2030" 0r Date of Birth ="10/20/2003" or Date of Birth ="10.20.2003" or Date of Birth ="10202003"
        - **Expected Outcome**: Error message "Invalid Date of Birth format. Please use MM/DD/YYYY."

### **3. Shipping Cost Changes**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Place order of exactly €20 after discounts.
        - **Input**: Cart total after discount = €20
        - **Expected Outcome**: Free shipping applied.
2. **Boundary Value Analysis**:
    - **Test Case**: Place order of €19.99 after discounts.
        - **Input**: Cart total after discount = €19.99
        - **Expected Outcome**: €5 shipping fee applied.
4. **Equivalence Partitioning**:
   - **Test Case**: Place order significantly above €20.
       - **Input**: Cart total = €40
       - **Expected Outcome**: Free shipping applied.
5. **Equivalence Partitioning**:
   - **Test Case**: Place order clearly below €20.
       - **Input**: Cart total = €10
       - **Expected Outcome**: €5 shipping fee applied.
6. **Use Case Testing**:
   - **Test Case**: Verify shipping fee display in cart and checkout page.
       - **Input**: Cart total = €15
       - **Expected Outcome**: €5 shipping shown in both cart and checkout page.













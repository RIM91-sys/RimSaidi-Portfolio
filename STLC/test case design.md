**Design your test cases based on the features that will be developed for the upcoming release of the online grocery shop!**

**You only have to design them, the execution will happen in a later phase.**

**Add the test design technique, if applicable.**

Example software: ShopFresh

### **1. Product Rating and Reviews**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify submission of a review with exactly 200 characters.
        - **Input**: Review text = 200 characters, Rating = 5 stars
        - **Expected Outcome**: Review is submitted successfully and displayed on the product page.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify submission of a review when review exceeds 200 characters.
        - **Input**: Review text = 201 characters, Rating = 4 stars
        - **Expected Outcome**: Error message: "Review must not exceed 200 characters."
3. **Equivalence Partitioning**:
    - **Test Case**: Submit a rating without text.
        - **Input**: Rating = 3 stars, Review text = empty
        - **Expected Outcome**: Review submitted successfully (since text is optional) and shown under product reviews.
4. **Error Guessing**:
    - **Test Case**: Submit a review with inappropriate language.
        - **Input**: Review = "This product is ****", Rating = 2 stars
        - **Expected Outcome**: Error message: "Review contains inappropriate content."

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
        - **Expected Outcome**: Error message "Date of Birth is required."
5. **Error Guessing**:
    - **Test Case**: Verify system behavior when an invalid Date of Birth format is entered.
        - **Input**: Date of Birth = "10/20/2003"
        - **Expected Outcome**: Error message "Invalid Date of Birth format. Please use MM/DD/YYYY."

### **3. Shipping Cost Changes**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Place order of exactly €50 after discounts.
        - **Input**: Cart total after discount = €50
        - **Expected Outcome**: Free shipping applied.
2. **Boundary Value Analysis**:
    - **Test Case**: Place order of €49.99 after discounts.
        - **Input**: Cart total after discount = €49.99
        - **Expected Outcome**: €4 shipping fee applied.
4. **Equivalence Partitioning**:
   - **Test Case**: Place order significantly above €50.
       - **Input**: Cart total = €80
       - **Expected Outcome**: Free shipping applied.
5. **Equivalence Partitioning**:
   - **Test Case**: Place order clearly below €50.
       - **Input**: Cart total = €30
       - **Expected Outcome**: €4 shipping fee applied.
6. **Use Case Testing**:
   - **Test Case**: Verify shipping fee display in cart and checkout page.
       - **Input**: Cart total = €45
       - **Expected Outcome**: €4 shipping shown in both cart and checkout page.













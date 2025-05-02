# **Test Plan for Market Mate’s  Webshop New Features**
### **1. Analyze the Product**

**Objective**

Ensure the new features (Product Rating System, Age Verification for Alcoholic Products, and Shipping Cost Changes) work correctly, are user-friendly, secure, and improve the overall webshop experience without introducing defects.
**User Base**

Regular grocery shoppers

Users purchasing alcohol (adults 18+)

Registered and guest users

Business stakeholders (marketing, sales teams)

**Hardware and Software Specifications**

- **Hardware Requirements:**
    - Devices: PCs, laptops, smartphones, tablets
    - Specifications: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor
- **Software Requirements:**
    - Operating Systems: Windows, macOS, Android, iOS
    - Browsers: Chrome, Firefox, Safari, Edge
    - Dependencies: Backend services, third-party ad services, payment gateways

**Product Functionality**

**Existing Functionality:**
The product allows users to:

- Search for products
- Add products to the shopping cart
- Complete checkout and place orders
- Create and manage user accounts
- Process payments securely
**To Be Added Functionality:**
- Allow users to rate products with a 1–5 star system and optional written reviews (up to 200 characters), with the ability to edit or delete their reviews.
- Display ratings and reviews under a "Reviews" section on each product page, with profanity filtering.
- Implement age verification when accessing the "Alcohol" category by requiring users to enter their date of birth. Users under 18 are redirected to the homepage.
- Introduce free shipping for orders over €50 (after discounts), with a €4 shipping fee for orders below €50, visible in the cart and at checkout.

### **2. Design the Test Strategy**

**Scope of Testing**

- **In Scope:**
- Product search functionality
- Adding products to the shopping cart
- Checkout process and order placement
- User account creation and management
- Secure payment processing
- Submitting product ratings (1–5 stars) and optional written reviews (up to 200 characters)
- Editing and deleting submitted reviews
- Displaying ratings and reviews under a "Reviews" section with profanity filtering
- Age verification modal when accessing the "Alcohol" category
- Redirecting users under 18 years old after age verification
- Applying free shipping for orders over €50 and showing shipping costs in the cart and at checkout
- Display and calculation of shipping costs based on cart value

- **Out of Scope:**
- Long-term storage or reuse of user-provided age data
- Document upload or advanced identity verification for age checks
- International shipping rules or costs
- Backend database operations not visible to users (e.g., server-side review management)

**Type of Testing**

- Functional Testing: To verify that each new feature works according to the requirements (e.g., product search, add to cart, checkout).
- Regression Testing: To ensure that the new features do not negatively impact the existing functionalities.
- Usability Testing: To check if the new features are easy to use and user-friendly for customers.
- Performance Testing  (age verification pop-up response time): To confirm that the webshop performs well under load, especially during peak shopping times.
- Security Testing (profanity filter, validation checks): To identify any vulnerabilities introduced by new features, particularly around payments and user accounts.
- Compatibility Testing(different devices/browsers): To ensure the new functionalities work smoothly across different devices, browsers, and operating systems.
- User Acceptance Testing (UAT): To validate that the new features meet the expectations and needs of real users.

**Risks and Issues**

- **Delays in development**
    - Mitigation: Implement a buffer period in the schedule.
- **Lack of test data**
    - Mitigation: Create mock data sets for testing purposes.
- **Resource unavailability**
    - Mitigation: Identify backup resources.

**Test Logistics**

- **Jane Smith** - Test Manager
- **John Doe** - QA Engineer (Functional and Regression Testing)
- **Alice Johnson** - QA Engineer (Performance and Security Testing)
- **Robert Brown** - QA Engineer (Usability Testing)
- **Maria Garcia** - End User for UAT

### **3. Define Test Objectives**

**Objectives**

- **Functionality:** Ensure new features and existing functionalities work as intended.
- **GUI:** Verify the graphical user interface for usability and consistency.
- **Performance:** Confirm the system's performance under expected load conditions.
- **Security:** Identify and mitigate potential security vulnerabilities.
- **Usability:** Assess the user-friendliness of the platform.

**Expected Outcomes**

- **Functionality:** All features perform correctly according to specifications.
- **GUI:** The interface is intuitive, responsive, and free of defects.
- **Performance:** The platform meets performance benchmarks under load.
- **Security:** No significant vulnerabilities are detected.
- **Usability:** Users can navigate and use the platform easily.

### **4. Define Test Criteria**

**Suspension Criteria**

- Testing will be suspended if critical defects are found that block further testing.
- Lack of necessary resources or test environment failures.

**Exit Criteria**

- All planned tests have been executed.
- Run Rate: At least 95% of all test cases have been executed.
- Pass Rate: At least 90% of executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- Performance metrics meet the defined standards.
- Security vulnerabilities have been identified and addressed.
- User acceptance testing has been completed, and sign-off has been obtained.

### **5. Resource Planning**

- **Human Resources:** QA team, development team, end users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Browsers (Chrome, Firefox, Safari, Edge), operating systems (Windows, macOS, Android, iOS)
- **Infrastructure:** Test environments, automation tools, performance testing tools

### **6. Plan Test Environment**

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

### **7. Schedule and Estimation**

| Activity | Start Date | End Date | Environment | Responsible Person | Estimated Effort |
| --- | --- | --- | --- | --- | --- |
| Test Planning | 01/08/2024 | 05/08/2024 | All | Test Manager | 20 hours |
| Test Case Design | 06/08/2024 | 15/08/2024 | All | QA Team | 40 hours |
| Unit Testing | 16/08/2024 | 25/08/2024 | DEV | Development Team | 60 hours |
| Integration Testing | 26/08/2024 | 30/08/2024 | TEST | QA Team | 30 hours |
| System Testing | 01/09/2024 | 10/09/2024 | TEST | QA Team | 80 hours |
| Regression Testing | 11/09/2024 | 15/09/2024 | TEST | QA Team | 40 hours |
| Performance Testing | 16/09/2024 | 18/09/2024 | TEST | QA Team | 20 hours |
| Security Testing | 19/09/2024 | 21/09/2024 | TEST | QA Team | 20 hours |
| UAT | 22/09/2024 | 30/09/2024 | ACC | End Users | 50 hours |
| Production Release | 01/10/2024 | 01/10/2024 | PROD | DevOps Team | 10 hours |

### **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**
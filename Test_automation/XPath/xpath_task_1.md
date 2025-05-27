
1. XPath to locate the main **h1 element**:  //h1[@id='mainTitle']
2. XPath to select **the About Us** navigational link:   //a[text()='About Us']
3. XPath to select **the Graphic Design** dropdown link:   //ul[@class='dropdown']//a[text()='Graphic Design']
4. XPath to select the team member’s name **Jane Smith**:   //div[@class='team']//h4[text()='Jane Smith']
5. XPath to select the description (which is inside the paragraph) of **SEO Services**:   //div[@class='service-item'][h3='SEO Services']/p
6. XPath expression to select all service items in the **"Our Services"** section:   //section[@id='services']//div[@class='service-item']
7. XPath to select the **email input field** in the contact form:    //form[@id='contactForm']//input[@id='email']
8. XPath to select the **entire contact form**:    //form[@id='contactForm']
9. XPath to select the **footer paragraph element**:    //footer//p
10. XPath to select the **first team member's(< h4 >)** name:    //div[@class='team']//ul/li[1]/h4
11. XPath to select the description of the **second service** item:    //div[@class='service-item'][2]/p
12. XPath to select the **"Contact Us"** section header (< h2 > element):    //section[@id='contact']//h2
13. XPath to select all links within the dropdown under the "Services" navigation item:   //a[text()='Services']/following-sibling::ul[@class='dropdown']//a
14. XPath to select the first < li > under the "Our Team" section:    //div[@class='team']//ul/li[1]
15. XPath to locate the **"Send Message"** button in the contact form:    //form[@id='contactForm']//input[@type='submit' and @value='Send Message']


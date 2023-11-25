# FORKIDS

[Visit the website here](https://for-kids-1eb46f197086.herokuapp.com)

![screenshot](documentation/mockup.png)

This project was created as a web app application using Python within Django framework, ElephantSQL as a relational database system, Amazon Web Services, Stripe payment platform, Heroku cloud platform and more. The whole development proccess has been made using cloud IDE called CodeAnywhere. The project was made for educational purposes only.

The business goals for this website are:

1. To boost the ForKids brand awareness
2. To get more leads
3. To build a database of users - current and possibly future customers
4. To increase sales

The user goals for this website are:

| As a/an... | I want to be able to... | so that I can... |
| --- | --- | --- |
| website visitor | view products | select one to buy |
| | check every individual product details | identify the price, description, product rating or image |
| | see the total cost of my shopping at any time | avoid spending too much |
| | sort the products | easily identify the best rated, best priced or categorically sorted products |
| | search for a product by a name or description | find a specific product |
| | view items that I want to buy in my bag | check the total cost and all selected products |
| | adjust the quantity or items in my bag | easily make changes before checkout |
| | safely enter my payment and personal information | checkout quickly without any problems |
| | view an order confirmation after checkout | verify that I have not made any mistakes |
| | receive an email confirmation after checking out | keep the confirmation of the purchase |
| site user | easily register for an account | have a personal profile |
| | login, logout, or recover my password | access or recover my personal account information |
| | have a personalized user profile | view my order history or order confirmations |
| administrator | add products | add new items to my store |
| | edit a product | change product information |
| | delete a product | remove items that are no longer for sale |
| | check list of completed orders and users | have feedback of the website processes |

## UX

### **Strategy**

Considering the core UX principles, first I started to think about the strategy for this project and defined who the target users would be and what features/technologies they would want.

ForKids target users are kids, adults, parents or collectors. Anyone who loves toys in general and would like to buy them.

And now the question is - what would be these users looking for? The answers I found were:

* Clear navigation which is easy to follow
* Good looking design which makes the website look desirable
* Possibility to register, login and create the profile
* View products and sort them through multiple options, such as price or rating
* View products details
* Possibility to search through products
* Pay safely for products in a shopping bag
* Get a confirmation of their purchase
* Access to social media links to follow the news

This project has been built to offer all of the named things. An extra effort was taken to provide intuitive interaction for every user visiting the webpage.

### **Scope**

To achieve the desired user and business goals, the following features will be included in this release:

* 'Home' page with logo, navigation panel and search bar, hero image with information, call up button to check the available products, and also including the footer with social media links as well
* 'Products' page where the user can search through the shop by the navigation panel, search bar or sorting options
* Every product has it's details page which contains information such as category, rating, image, description. It can be opened upon clicking on the product
* The product detail includes the button 'Add to Bag' which will add the product to the shopping bag of the user
* 'Shopping Bag' page which shows the chosen products to buy, their price, delivery costs and the grand total
* 'Checkout' page which contains form to fill with the customer information, order summary and payment form
* 'Confirmation' page which shows up after the checkout was successfully done with order summary and confirmation
* 'Profile' page where users can save their delivery information for faster shopping and check order history
* 'Product management' page for an admin only to add products

### **Structure**

The app's Back End has been built by Python using Django framework because it's flexible and less time-wasting. All data are getting saved into PostgreSQL using ElephantSQL database system and fully accessible through the provided dashboard. Connection to the database has been coded through Python.

The website is made up of multiple apps using Django MTV method = Models, Templates and Views. Each built page has it's own app.
It's important to mention that I used Bootstrap for its design principles and grid system to make sure that responsiveness is on point.

A special user 'admin' can access the Django admin page, where he can add, edit or delete any category or product. He has also a possibility to see the users information, such as their profile name or email address.

All important actions give feedback to the user in the form of messages, for example after registration, adding a product or signing in.

### **Skeleton**

This project is about the Full Stack development - so I decided to focus not only on the Back End and logic part of the website, but Front End as well and tried to built as good design as possible.

I intentionally used CSS styling to make interaction with this web application handy, for example with text styling, shadow and hovering effects on buttons, product design and checkout page.

Last but not least, I worked on responsiveness to allow users to use the webpage on different devices without any additional errors.

I felt that all mentioned above helps to provide the best User Experience and highlight the purpose of this project.

### Color Scheme
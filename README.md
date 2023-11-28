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

Considering the core UX principles, as first I started to think about the strategy for this project and defined who the target users would be and what features/technologies they would want.

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

This project has been built to offer all of the named things. An extra effort was taken to provide an intuitive interaction for every user visiting the webpage.

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

With help of Django, it was easier to implement the logic part of this project and it's clearly visible in examples like checkout where a user can have his details already loaded from profile, or in 'My Profile' page where he can find his order history and upload the information needed for completing the order.

### **Skeleton**

This project is about the Full Stack development - so I decided to focus not only on the Back End and logic part of the website, but Front End as well and tried to built as good looking page as possible.

I intentionally used CSS styling to make interaction with this web application handy, for example with text styling, shadow and hovering effects on buttons, product design and checkout page.

Last but not least, I worked on responsiveness to allow users to use the webpage on different devices without any additional errors. Creating something responsive is integral to the design.

I felt that all mentioned above helps to provide the best User Experience and highlight the purpose of this project.

### Color Scheme

I chose a color palette based around white & black as these colors are elegant and simple to implement into the design. I added green colors for buttons and headings. Additionally, I chose to use other colors for hover effects and box shadowing, however the main palette has been around these colors:

* `#000000` used for primary text or background
* `#ffffff` used for secondary text or background
* `#4B8351` used for primary highlights
* `#787F7E` used for secondary highlights

The colours have been mainly used with help of Bootstrap framework.

![screenshot](documentation/coolors.png)

### Typography

I decided to use Google font 'Lato' with different font weights throughout the project thanks to its elegance. I left the font 'sans-serif' as a backup font style if anything goes wrong with the Google link. Secondly, I used the Google font 'Metal Mania' for the logo of the website.

* [Lato](https://fonts.google.com/specimen/Lato)

* [Sans-serif](https://fonts.google.com/knowledge/glossary/sans_serif)

* [Metal Mania](https://fonts.google.com/specimen/Metal+Mania)

## Wireframes

To follow the best practices, wireframes were developed for mobile, tablet, and desktop sizes.

## Features

### Existing Features

* **Home Page**

'Home Page' contains the navigation menu on the top with the logo, searchbar for the user to use, links to the account and shopping bag. I decided to use the hero image with call-to-action button in the middle that opens the products page. As the last piece, there is the footer on the bottom of the page which contains the social media links.

![screenshot](documentation/mockup.png)

* **Searchbar**

In the middle of the navigation panel (when using desktop view, otherwise as an icon shown in the next feature) is placed the search bar which is meant to help people to search through the products on the webpage. In the example below, I tried to find the 'cards' and it showed me result with cards as the product/category name or in description.

![screenshot](documentation/use_search.png)

* **Navigation Panel**

As part of the responsive design, I have to be sure that the navigation is always visible and accessible to the user. That's why I used the dynamic navbar from Bootstrap. It follows the chosen UX principles and adds a nice touch when the user uses a smaller device. The best point is that all the features remains accessible to the user at anytime.

![screenshot](documentation/nav_panel.png)

* **Products Page**

![screenshot](documentation/products_page.png)

* **Product Details Page**

![screenshot](documentation/product_details_page.png)

* **Messages**

![screenshot](documentation/messages.png)

* **Shopping Bag Page**

![screenshot](documentation/shopping_bag_page.png)

* **Checkout Page**

![screenshot](documentation/checkout_page.png)

* **Webhook Handler**

![screenshot](documentation/webhook_handler.png)

* **Order Confirmation Page**

![screenshot](documentation/order_confirmation.png)
![screenshot](documentation/stripe_payment.png)

* **Sign In Page**

When the user is already registered, he can sign in using this page. The path for signing in goes through My Account button in the navigation panel.

![screenshot](documentation/sign_in_page.png)

* **Sign Up Page**

![screenshot](documentation/sign_up_page.png)

* **Profile Page**

![screenshot](documentation/profile_page.png)

* **Product Management Page**

![screenshot](documentation/product_management_page.png)

* **Django Admin**

![screenshot](documentation/django_admin.png)

* **Favicon**

As a rule of thumb, I added the Favicon which relates to the topic of the project.

![screenshot](documentation/favicon.png)

### Future Features

## Tools & Technologies Used

* [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content
* [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) used for user interaction on the site
* [Python](https://www.python.org) used as the back-end programming language
* [Django](https://www.djangoproject.com) used as the Python framework for the site
* [Git](https://git-scm.com) used for version control (`git add`, `git commit`, `git push`)
* [GitHub](https://github.com) used for secure online code storage
* [Heroku](https://heroku.com) used for hosting the deployed back-end site
* [CodeAnywhere](https://codeanywhere.com) used as a cloud-based IDE for the development
* [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components
* [Font Awesome](https://fontawesome.com/) used to obtain the media icons
* [Google Fonts](https://fonts.google.com/) used to obtain the fonts linked in the header and used in the project
* [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools) used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project
* [Grammarly](https://www.grammarly.com/) used to fix the thousands of grammar errors across the project
* [Coloors](https://coolors.co/) used to create a color palette for the design
* [W3C Markup Validation Service](https://validator.w3.org/) used to validate all HTML code written and used on this webpage
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) used to validate all CSS code written and used on this webpage
* [JSHint](https://jshint.com/) used to validate all JS code written and used on this webpage
* [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) used to validate all of my Python files
* [Lucid](https://www.lucidchart.com/pages/examples/er-diagram-tool) used to design the database ER diagram
* [PostgreSQL](https://www.postgresql.org) used as the relational database management
* [ElephantSQL](https://www.elephantsql.com) used as the Postgres database
* [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services
* [AWS S3](https://aws.amazon.com/s3) used for online static file storage

## Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| from [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Pexels](https://www.pexels.com/photo/toy-military-vehicles-5257289/) | home page | background image | hero image |

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project. Here is one example of created model and shown it's data in the table:

```python
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

* Table: **Product**

    | **PK** | **id** (unique) | Type | Notes |
    | --- | --- | --- | --- |
    | **FK** | category | ForeignKey | FK to **Category** model |
    | | sku | CharField | |
    | | name | CharField | |
    | | description | TextField | |
    | | price | DecimalField | |
    | | rating | DecimalField | |
    | | image_url | URLField | |
    | | image | ImageField | |

I have used [Lucidchart](https://www.lucidchart.com/) to design my site ERD. The entire data schema is shown in the screenshot below:

![screenshot](documentation/erd.png)

# Testing

# Deployment

The live deployed application can be found on [Heroku](https://for-kids-1eb46f197086.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

* Click **Create New Instance** to start a new database.
* Provide a name (this is commonly the name of the project: ForKids).
* Select the **Tiny Turtle (Free)** plan.
* You can leave the **Tags** blank.
* Select the **Region** and **Data Center** closest to you.
* Once created, click on the new database name, where you can view the database URL and Password.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, because of the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

* Search for **S3**.
* Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
* Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
* From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
* From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
* From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

* Copy your **ARN** string.
* From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
  * Policy Type: **S3 Bucket Policy**
  * Effect: **Allow**
  * Principal: `*`
  * Actions: **GetObject**
  * Amazon Resource Name (ARN): **paste-your-ARN-here**
  * Click **Add Statement**
  * Click **Generate Policy**
  * Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

  * Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
  * Click **Save**.

* From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
  * If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

* From **User Groups**, click **Create New Group**.
  * Suggested Name: `group-forkids` (group + the project name)
* Tags are optional, but you must click it to get to the **review policy** page.
* From **User Groups**, select your newly created group, and go to the **Permissions** tab.
* Open the **Add Permissions** dropdown, and click **Attach Policies**.
* Select the policy, then click **Add Permissions** at the bottom when finished.
* From the **JSON** tab, select the **Import Managed Policy** link.
  * Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
  * You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```

  * Click **Review Policy**.
  * Suggested Name: `policy-forkids` (policy + the project name)
  * Provide a description:
    * "Access to S3 Bucket for forkids static files."
  * Click **Create Policy**.
* From **User Groups**, click your "group-forkids".
* Click **Attach Policy**.
* Search for the policy you've just created ("policy-forkids") and select it, then **Attach Policy**.
* From **User Groups**, click **Add User**.
  * Suggested Name: `user-forkids` (user + the project name)
* For "Select AWS Access Type", select **Programmatic Access**.
* Select the group to add your new user to: `group-forkids`
* Tags are optional, but you must click it to get to the **review user** page.
* Click **Create User** once done.
* You should see a button to **Download .csv**, so click it to save a copy on your system.
  * **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
  * This contains the user's **Access key ID** and **Secret access key**.
  * `AWS_ACCESS_KEY_ID` = **Access key ID**
  * `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

* If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
* Back within **S3**, create a new folder called: `media`.
* Select any existing media images for your project to prepare them for being uploaded into the new folder.
* Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
* No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

* From your Stripe dashboard, click to expand the "Get your test API keys".
* You'll have two keys here:
  * `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
  * `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

* From your Stripe dashboard, click **Developers**, and select **Webhooks**.
* From there, click **Add Endpoint**.
  * `https://for-kids-1eb46f197086.herokuapp.com/checkout/wh/`
* Click **receive all events**.
* Click **Add Endpoint** to complete the process.
* You'll have a new key here:
  * `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

* Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
* Click on the **Accounts and Import** tab.
* Within the section called "Change account settings", click on the link for **Other Google Account settings**.
* From this new page, select **Security** on the left.
* Select **2-Step Verification** to turn it on. (verify your password and account)
* Once verified, select **Turn On** for 2FA.
* Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
* This might prompt you once again to confirm your password and account.
* Select **Mail** for the app type.
* Select **Other (Custom name)** for the device type.
  * Any custom name, such as "Django" or ForKids
* You'll be provided with a 16-character password (API key).
  * Save this somewhere locally, as you cannot access this key again later!
  * `EMAIL_HOST_PASS` = user's 16-character API key
  * `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

* Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
* Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
* From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

* requirements.txt
* Procfile

You can install this project's **requirements** (where applicable) using:

* `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

* `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

* `echo web: gunicorn app_name.wsgi > Procfile`
* *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

* Select **Automatic Deployment** from the Heroku app.

Or:

* In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
* Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
* After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  * `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

* `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

* Start the Django app: `python3 manage.py runserver`
* Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
* Make any necessary migrations: `python3 manage.py makemigrations`
* Migrate the data to the database: `python3 manage.py migrate`
* Create a superuser: `python3 manage.py createsuperuser`
* Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
* Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

* `python3 manage.py dumpdata your-model > your-model.json`
* *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JakBul/ForKids)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	* `git clone https://github.com/JakBul/ForKids.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JakBul/ForKids)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JakBul/ForKids)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README | Tool to help generate the Markdown files |

## Acknowledgments

* First and foremost, I would like to thank my Code Institute mentor Rohit for his support throughout the development of this project
* In addition, I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support

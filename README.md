
# SHOP EASY


![GitHub contributors](https://img.shields.io/github/contributors/alexandergrib/ms4-store)
![GitHub last commit](https://img.shields.io/github/last-commit/alexandergrib/ms4-store)
![GitHub language count](https://img.shields.io/github/languages/count/alexandergrib/ms4-store)
![Font Awesome version](https://img.shields.io/badge/Font%20Awesome-v5.15.1-blue)
![Travis CI Build](https://secure.travis-ci.org/abibubble/ms4-lead-shot-hazard.png)

[//]: # (![Testing coverage]&#40;https://img.shields.io/badge/coverage-92%25-brightgreen&#41;)
![GitHub forks](https://img.shields.io/github/forks/alexandergrib/ms4-store?style=social)

[Here is a link to the final project](https://ms4-store.herokuapp.com/)

This site is a printer and cartridges e-commerce site for my fried who owns small business in Russia. Website eventually would bee translated in to russian. This site is fully responsive on all modern screen sizes, and it allows the admin to easily add, edit or delete products that he have to sell.

This site was built using HTML, CSS, Bootstrap, JavaScript, jQuery, Python, Django, and it uses a SQL database through PostgreSQL.

---



---

## Icon key

&#128272; <-- Superuser only access

&#128100; <-- Logged In Only

&#128683; <-- Logged Out only

&#9989; <-- Yes / Visible

&#10060; <-- No / Not visible

[Back to the top](#SHOP EASY)

---


## User Experience

## Initial Discussion

* I wanted to create a website linked to a database, which allows users to log in, search for, and find printers and cartridges for them.
* Currently, I have a basic one-page website, and I think it's a time to upgrade to bring more customers in, and be able to manage products more easily
* I wanted to be able to add, edit and delete items of products for sale.

## Site Owner's Goals
 - As a site owner, I want to be able to add new or edit existing products.
 - As a site owner, I want to be able to remove existing products.
 - As a site owner, I want to be able to add new/existing products to "special offers/sale".
 - As a site owner, I want to be able to add new, edit or remove existing categories and brands.

## First Time Visitor Goals
 - As a Shopper, I want to be able to view a list of products, so that I can select some to purchase.
 - As a Shopper, I want to be able to view individual product details, product Image, the price, the product description and the compatible cartridges.
 - As a Shopper, I want to look for testimonials to understand what other users think of the site and the service it renders.
 - As a First Time Visitor, I want to sign up to the site to enable me full access to it's service and also to receive email newsletter and latest updates.

## Returning Visitor Goals

  - As a Returning Visitor, I want to see new products and deals.
  - As a Returning Visitor, I want to find the best way to get in contact with the site owner with any questions I may have.
  - As a Frequent User, I want to be able to log in to the site view my profile and add items to wishlist.

## Frequent User Goals
 - As a Frequent User, I want to browse the site to see if there are any changes, new deals and/or clearance items.
 - As a Frequent User, I want to see information about the most new arrivals and sales.
 - As a Frequent User, I want to be able to sort products by price, category, or brand


---

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://en.wikipedia.org/wiki/Jquery)
-   [Python3](https://en.wikipedia.org/wiki/Python_Programming_Language)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.x:](https://getbootstrap.com/)
    - Bootstrap 5.x was used to assist with the responsiveness and styling of the website.
2. [Font Awesome 5:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
3. [jQuery:](https://jquery.com/)
    - jQuery came with bootstrap to make the navbar entire site responsive.
4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git. 
6. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
7. [Heroku:](https://heroku.com/)
    - Heroku was used to create  and deploy our app.    
8. [Django:](https://django.com/)
    - Django was used to create the framework.
9. [Postgresql:](https://postgresql.org/)
    - Mongodb was used to create database and to connect server to our site.
10. [Stripe:](https://stripe.com/)
    - Stripe was used to accept and authorise payment for any item purchased on the site.
11. [AWS:](https://s3.console.aws.amazon.com/)
    - Amazon S3 was used to manage and save media and collectstatic file in Its cloud service.        


---


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [Lighthouse](https://https://developers.google.com/web/tools/lighthouse) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a Shopper, I want to be able to view a list of products, so that I can select an item to purchase.

      1. Upon entering the site. The homepage navigation bar have links to list of products and categories, user have the option to view all products or search for a specific product. ![](media/ms4screenshot1.jpeg)

    2. As a Site User, I want to be able to register for an account and have a personalised user profile.

      1. The Site User can register to view their personal order history and order confirmations, and save their payment information by clicking on My Area icon on the homepage top-right as shown on the screenshot above.

    3. As a First Time Visitor, I want to locate the site social media links to see past and present post about the site service.
       
      1. The social media links is on the footer on every page of the site. !

-   #### Returning User Goals

    1. As a Returning User, I want to see information about new products.

      1. Returning user can find contents about new products on the home page or click on New Arrivals link on the navbar. ![](media/ms4screenshot3.jpeg) 
    
    2. As a Returning Visitor, I want to find the best way to get in contact with customer service with any questions I may have.

      1. Returning Visitor can contact customer service through contact us link on the footer of the site.

-   #### Frequent User Goals

    1. As a Frequent User, I want to see updates about any change, sales, or new products on the site.

      1. Frequent User can easily find this updates and contents on the home page. !

    2. As a Frequent User, I want to check to see if there are any new blog posts.

      1. The social media links is on the footer with links to the site blog and social post.


### Further Testing

-   The Website was tested on Google Chrome, Mozilla Firefox, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone SE, iPhone 11, One+ 9 Pro, and iPadPro.
-   A large amount of testing was done to ensure that all pages were linking correctly
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   

### Known Issues

-


---

## Credits

### Code

-   Codes were copied and modified from the Full Stack Frameworks with Django, Boutique Ado Project.

-   Bootstrap5 template was used throughout the project mainly to make site responsive using the [bootsrap 5](https://getbootstrap.com/)

### Content

-   All content was written by the developer.

### Media

-   All Images belong to the copyright owner.

### Acknowledgements

- Student Care and Tutor at Code Institute for their support.


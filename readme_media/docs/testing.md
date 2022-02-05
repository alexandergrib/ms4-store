# Return to [README.md](https://github.com/alexandergrib/ms4-store/blob/main/README.md)
# Testing Steps


[Back to the top](#testing-steps)

---

## Automated Testing

Automated Unit Testing was done using [Django’s testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/) and [Travis CI](https://www.travis-ci.com/)'s continuous integration testing functionality.


### Django Testing

### Bag app

#### Bag views

- Test the view_bag URL
- Test the add_to_bag URL
- Test that the add_to_bag view adds a product to the shopping bag
- Test the adjust_bag URL
- Test the remove_from_bag URL
- Test the add_to_bag view
- Test that the add_to_bag view updates the quantity of an item if it already exists in the bag
- Test the adjust_bag view
- Test that the adjust_bag view removes the item when the quantity is less than 1
- Test the remove_from_bag view
- Test that the remove_from_bag view throws an error if something goes wrong


#### Bag Others

- Test that the delivery cost is calculated correctly
- Test that the calc_subtotal function works

#### Coverage Report

![bag app coverage](./readme_media/bag_app_coverage.png)

---

### Checkout App

#### Checkout Forms

- Test that full name is required
- Test that email is required
- Test that phone_number is required
- Test that country is required
- Test that town_or_city is required
- Test that street_address1 is required
- Test that the form fields are correct in the meta class

#### Checkout Models

- Test that the order string method returns the order number
- Test the checkout_details model
- Test the update_total model
- Test that the OrderLineItem string method returns the correct string

#### Checkout Views

- Test the cache_checkout_data view
- Test that the Checkout page URL exists
- Test that the Checkout page URL is accessible by name
- Test that the Checkout page uses the correct template
- Test that an error displays when there is nothing in the shopping bag
- Test that an error displays when the Stripe key isn't set
- Test the get in the checkout view
- Test that the user's details are auto-filled if the user is logged in and has saved information



#### Coverage Report

![checkout app coverage](./readme_media/checkout_app_report.png)

---

### Home App

#### Home Views

- Test that the Home page URL exists
- Test that the Home page URL is accessible by name
- Test that the Home page uses the correct template



#### Coverage Report

![home app coverage](./readme_media/home_app_coverage.png)

---

### Products App

### Products Models

- Test the product name
- Test the product description
- Test the product has_sizes
- Test the category name
- Test the category friendly_name

### Products Views

- Test that the Products page URL exists
- Test that the Products page URL is accessible by name
- Test that the Products page uses the correct template
- Test the products page view

### Test the categories view

- Test the product_detail view
- Test that the product detail page URL exists
- Test the product sort functionality
- Test the product search functionality
- Test the product search error message shows correctly
- Test that a regular user cannot access the add a product page
- Test that the add a product page displays for a superuser
- Test that a regular user cannot access the edit a product page
- Test that the edit a product page displays for a superuser
- Test that a regular user cannot access the delete a product view
- Test that the delete a product view works for a superuser


#### Coverage Report

![products app coverage](./readme_media/products_app_coverage.png)

---

#### Profiles

##### Profiles Forms

- Test that the user profile form fields aren't required
- Test the meta class of the user profile form

##### Profiles Models

* Test the getting user profile model

##### Profiles Views

- Test that the Profiles page URL exists
- Test that the Profiles page URL is accessible by name
- Test that a logged-in user can view the profile
- Test that the profile information gets saved correctly
- Test that the order history displays when requested


#### Coverage Report

![profiles app coverage](./readme_media/profiles_app_coverage.png)


### Total Coverage Report

![all apps combined coverage](./readme_media/full_coverage.png)


---

### Travis CI

![Travis CI Build](https://app.travis-ci.com/alexandergrib/ms4-store.svg)

[Click here to view the Travis CI full build report](./readme_media/travis_build_history.png)

[Back to the top](#testing-steps)

---


## Manual Testing


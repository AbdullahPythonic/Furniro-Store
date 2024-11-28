# Furniro Store(E-Commerce Website)

This is a full-featured e-commerce application built with Django. The project includes essential e-commerce features such as a shopping cart, product management, user registration, login, checkout, and order management, all developed with clean and simple code.


## Features

- **Categorized Products:** User can see Product by Categories.
- **Product Listing:**  Users can browse all the listed products.
- **Product Detail:**  Users can see the detail of the product like description and also can see the related products.
- **Shopping Cart:** Users can add items to the cart, adjust quantities, and remove items.
- **Checkout Process:** A streamlined checkout with order summary, user details, and payment method options.
- **Order Management:** Orders are saved, and stock levels are updated upon purchase.
- **Responsive Design:** User-friendly across various screen sizes.


## Technologies Used

- **Django:** Backend framework for handling data and serving the site.
- **HTML/CSS:** Frontend structure and styling.
- **JavaScript:** For interactive elements, such as quantity selectors.


## Project Structure

.
- ├── Cart/
- │   ├── migrations/
- │   ├── templates/
- │   │   └── cart/
- │   └── static/
- │       └── cart/
- ├── Categories/
- │   ├── migrations/
- │   ├── templates/
- │   │   └── categories/
- │   └── static/
- │       └── categories/
- ├── Product/
- │   ├── migrations/
- │   ├── templates/
- │   │   └── product/
- │   └── static/
- │       └── product/
- ├── Checkout/
- │   ├── migrations/
- │   ├── templates/
- │   │   └── checkout/
- │   └── static/
- │       └── checkout/
- └── manage.py


## Models

Each app has its own set of models. Here’s a summary:
- **Product:** Model to manage product details.
- **Category:** Model for product categories.
- **Cart:** Manages items in the user's cart.
- **Checkout:** Handles user orders and checkout information.


## Screenshots

- **Home page**
![Homepage Screenshot](screenshots/home.jpeg)

- **All Products**
![All Products Screenshot](screenshots/shop.jpeg)

- **Categorized Products**
![Categorizes Screenshot](screenshots/categorized-products.jpeg)

- **Product Detail**
![product detail Screenshot](screenshots/product-detail.jpeg)

- **Cart**
![Cart Screenshot](screenshots/cart.jpeg)

- **Checkout**
![Checkout Screenshot](screenshots/checkout.jpeg)

- **Order Success**
![Order Screenshot](screenshots/order-success.jpeg)

- **Contact Us**
![Contact Screenshot](screenshots/contact.PNG)


## Future Improvments

- **Payment Gateway Integration**: Add an external payment gateway for secure payments.
- **Product Recommendations:** Suggest similar products to users based on their browsing history.
- **Order Tracking:** Allow users to track the status of their orders.
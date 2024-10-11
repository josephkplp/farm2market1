
# Farm2Market

Farm2Market is a Django-based web platform that connects farmers, producers, distributors, and customers, enabling them to manage agricultural value chains seamlessly. It offers functionalities for registering accounts, browsing products, adding them to a shopping cart, and interacting with sellers in a secure, user-friendly, and responsive environment.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Custom Template Filters](#custom-template-filters)
- [Static and Media Files](#static-and-media-files)
- [Usage](#usage)
- [Development Workflow](#development-workflow)
- [Deployment](#deployment)
- [License](#license)
- [Contributing](#contributing)

## Introduction

Farm2Market is a platform designed to optimize and integrate agricultural processes. The project is tailored for various stakeholders such as:

- Farmers: Showcase and sell their products (e.g., Irish potatoes, beans, goats, sheep, etc.).
- Producers: Facilitate the production and supply of raw materials.
- Distributors: Efficiently manage and distribute products.
- Customers: Explore, compare, and purchase agricultural goods in an intuitive marketplace.

The system is built with Django and features responsive front-end design, user authentication, product listings, and social login options. It emphasizes modularity, scalability, and security.

## Features

- User Authentication:
  - Secure registration and login system with form validation.
  - Social login options (Google, Microsoft, Apple).
  
- Product Management:
  - Product listings including details for items like Irish potatoes, beans, goats, sheep, ginger, tomatoes, and maize etc
  - Product detail pages for better user interaction.
  
- Shopping Cart:
  - Add products to cart, modify quantities, and view total prices.
  
- Responsive Design:
  - Mobile and desktop-friendly interface using CSS and Bootstrap.
  
- Custom Filters:
  - A `multiply` custom template filter used for product price calculation in the cart.

## Technology Stack

- Backend: Django 5.1.2, Python 3.12
- Frontend: HTML5, CSS3, Bootstrap, JavaScript
- Database: SQLite (default for development)
- Other Tools:
  - Custom template filters for enhanced functionality.
  - Integration of CSRF protection and secure transactions.

## Project Structure
farm2market/
├── products/
│   ├── migrations/                 # Django database migrations for product-related models
│   ├── static/
│   │   └── css/
│   │       └── register.css        # Styles specific to the registration page
│   ├── templates/
│   │   ├── base.html               # Base layout template for the entire application
│   │   ├── product_list.html       # Template for listing products
│   │   ├── product_details.html    # Template for product details view
│   │   └── registration/
│   │       └── register.html       # User registration template
│   ├── admin.py                    # Django admin customizations for products
│   ├── apps.py                     # Application configuration
│   ├── filters.py                  # Custom filters (e.g., multiply)
│   ├── models.py                   # Database models for products and categories
│   ├── urls.py                     # URL routing for products app
│   ├── views.py                    # Views handling product listing, detail pages, etc.
│   └── forms.py                    # Django forms for registration and product management
├── farm2market/
│   ├── settings.py                 # Django project settings
│   ├── urls.py                     # Project-level URL routing
│   ├── wsgi.py                     # WSGI configuration for deployment
│   ├── asgi.py                     # ASGI configuration for async support
├── media/                          # Directory for uploaded product images and files
├── static/                         # Global static files (CSS, JS, images, etc.)
├── templates/
│   └── 404.html                    # Custom 404 error page template
├── manage.py                       # Django management script
├── db.sqlite3                      # SQLite database (for development)
└── README.md                       # Project documentation (this file)


## Installation

To get the project up and running on your local machine, follow these steps:

### Prerequisites

- Python 3.12+
- pip (Python package installer)
- Virtualenv (recommended)

### Steps

1. Clone the repository:

  
   git clone https://github.com/yourusername/farm2market.git

2. Navigate to the project directory:

  
   cd farm2market


3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
  

4. **Install the project dependencies**:

   pip install -r requirements.txt
  

5. Apply migrations to set up the database:
   python manage.py migrate
 
6. Run the development server:
   python manage.py runserver
 
7. Access the application at `http://localhost:8000`.

## Configuration

### Static and Media Files

Ensure your project is set up to handle static and media files:

In `settings.py`, add the following configurations for handling media and static files:

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


### Favicon Integration

To add a favicon to the website, use a favicon generator like [favicon.io](https://favicon.io/) and save it in your `static` directory. In the `base.html` file, include the following:


<link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">


## Custom Template Filters

A custom Django template filter (`multiply`) is used to multiply the price of a product by its quantity in the cart.

### Adding the Filter

The filter is defined in `products/filters.py`:


from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg


To use the filter in your templates:


<td>${{ item.product.price|multiply:item.quantity }}</td>


## Usage

### Registering and Logging in Users

To allow users to register:

1. Navigate to `/register/` on the frontend.
2. Users can fill in their username, email, and password.
3. Upon registration, users can log in and start exploring products.

### Product Management

- Browse products via the product listing page.
- Click on any product for more details and add it to the cart.

## Development Workflow

1. Feature Development: Develop features in separate branches, and ensure to follow the best coding practices.
2. Testing: Always test new features locally before merging them into the main branch.
3. Code Review: Make pull requests, and ensure code is peer-reviewed.
4. Migrations: Always run migrations after any database-related changes using `python manage.py migrate`.

## Deployment

To deploy the application:

1. Set up a production server (e.g., using Gunicorn, Nginx, or Apache).
2. Use a production database like PostgreSQL.
3. Set the `DEBUG` setting in `settings.py` to `False`.
4. Ensure that static files are correctly served using:

   python manage.py collectstatic

5. For a smooth production environment, ensure SSL is enabled for secure transactions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request, ensuring that your code is well-tested and aligns with the project’s goals.


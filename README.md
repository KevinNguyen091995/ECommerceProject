## E-Commerce Project Objective
- The objective was to employ Django as an MVT framework and harness its full capabilities to construct a demonstration E-Commerce Web Application. This involved establishing Models, defining relationships, and utilizing the ORM for optimal functionality.
- Develop views to manage the presentation logic, encompassing product listings, individual product pages, user authentication procedures, and the administration of shopping carts. Take advantage of Django's class-based views to enhance efficiency and promote code reusability.
- Craft HTML templates for rendering page content, employing the Django template language for dynamic data rendering sourced from views.
- Implement forms to handle user input, facilitating actions like adding products to a shopping cart or completing an order.
- Employ Django's integrated authentication system for seamless handling of user registration, login, and logout processes.
- Configure URLs to seamlessly map to respective views, ensuring a well-organized and accessible web application structure.

## Features
- Account Registration
- Login/Logout
- Product List
- Product Detail View
- Sellers Listing Product
- Add To Cart
- Fake Purchase

## Future Features
- Django Rest Framework
  - Create Token and Authenticate API Calls
  - List Products and Seller information
  - Top Sellers and Images

# How to Setup
## 1. GitClone Project or Download ZIP
- git clone https://github.com/KevinNguyen091995/ECommerceProject.git
  
## 2. Create a Python Virtual Enviroment
- Open CMD or Terminal within cloned directory
- python -m venv env (Creates directory env with dependencies)

## 3. Start your virtual enviroment
- Windows : ./env/Scripts/activate
- Linux : source ./env/Scripts/activate

## 4. Install Django Package and libraries required for package
- pip install Django, django-bootstrap-v5, Pillow

## 5. Run Server
Within ECommerce Directory
- python manage.py runserver

## 6. Mess Around
To Create SuperUser for Django Admin
- python manage.py createsuperuser (Enter Username, Password)
- To add products or users via admin visit 127.0.0.1:8000/admin

URLs/URI/Endpoints
- 127.0.0.1:8000/register
- 127.0.0.1:8000/login
- 127.0.0.1:8000/products
- 127.0.0.1:8000/cart

## E-Commerce Project

## Features
- Account Registration
- Login/Logout
- Product List
- Product Detail View
- Sellers Listing Product
- Add To Cart
- Fake Purchase

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
- 
## 6. Mess Around
To Create SuperUser for Django Admin
- python manage.py createsuperuser (Enter Username, Password)
- To add products or users via admin visit 127.0.0.1:8000/admin

URLs/URI/Endpoints
- 127.0.0.1:8000/register
- 127.0.0.1:8000/login
- 127.0.0.1:8000/products
- 127.0.0.1:8000/cart

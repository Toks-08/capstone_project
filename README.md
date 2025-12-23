# E-Commerce API

## Overview

This is a **Django REST Framework-based e-commerce API** that allows users to browse products, manage a cart, and handle user authentication. The project is designed to be modular, scalable, and ready for deployment to production.

Key features include:

- Product and category management
- User registration and authentication (JWT tokens)
- Shopping cart management
- Product search functionality
- Admin-only permissions for sensitive operations
- RESTful API endpoints

---

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Challenges Faced](#challenges-faced)
- [Next Steps](#next-steps)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

---

## Setup

Run the development server:

```bash
python manage.py runserver
```

Access the API at `http://127.0.0.1:8000/`.\
Admin panel is available at `http://127.0.0.1:8000/admin/`.

---

## Environment Variables

Create a `.env` file at the project root and add the following:

```
SECRET_KEY=<your-django-secret-key>
DEBUG=True
```

---

## API Endpoints

### Authentication

- **POST** `/api/register/` – Register a new user
- **POST** `/api/login/` – Obtain JWT token



### Products & Categories

- **GET** `/api/product/` – List all products
- **GET** `/api/product/<id>/` – Retrieve a single product
- **POST** `/api/product/` – Create a new product (Admin only)
- **GET** `/api/category/` – List all categories
- **POST** `/api/category/` – Create a new category (Admin only)

### Cart

- **GET** `/api/cart/` – Retrieve current user’s cart
- **POST** `/api/cart/add/` – Add item to cart
- **POST** `/api/cart/remove/` – Remove item from cart

### Search

- **GET** `/api/product/search/?q=<query>` – Search for products by name or description

---

## Project Structure

```
ecommerce_project/
├── accounts/          # User authentication app
├── products/          # Product and category management
├── cart/              # Cart management
├── ecommerce_project/ # Project settings
├── manage.py
└── requirements.txt
```

---

## Technologies Used

- Python 3.11+
- Django 4.x
- Django REST Framework
- SQLite (default, for development)



---

## Challenges Faced

- Implementing search functionality with DRF filters
- Handling permissions for admin vs. regular users
- Managing cart items and ensuring correct serialization

---

## Next Steps

- Implement order management (checkout, payment integration)
- Add product reviews and ratings
- Implement pagination and filtering for product endpoints
- Deploy to production (PythonAnywhere / Render / Heroku)
- Write automated tests for all endpoints


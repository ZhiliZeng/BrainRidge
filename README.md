# Banking Transactions API

## Overview
This is a simple banking transactions API designed to handle user accounts and transactions between these accounts. The API is built using Django and follows a RESTful architecture. It supports the following operations:

Create a new user account with an initial balance.
Transfer funds from one account to another.
Retrieve the transaction history for a given account.

## Features
User Account Management: Create and manage user accounts with initial balances.
Fund Transfer: Transfer funds between accounts with proper validation.
Transaction History: Retrieve the transaction history for a given account.

## Requirements
Python 3.7+
Django 3.2+
Django REST framework



## Setup

1. Clone the repository:
   ```sh
   git clone <https://github.com/ZhiliZeng/BrainRidge/>
   cd banking

2. Install dependencies:
  ```sh
  pip install -r requirements.txt
```


  
3. Run migrations:
  ```sh
  python manage.py makemigrations
  python manage.py migrate
```

4. Run the development server:
  ```sh
  python manage.py runserver

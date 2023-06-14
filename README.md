# Application for Managing Clients in PostgreSQL

This application allows you to manage client information in a PostgreSQL database. You can add new clients, update their information, delete them, and more.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- PostgreSQL: [Download PostgreSQL](https://www.postgresql.org/download/)
- Python 3: [Download Python](https://www.python.org/downloads/)

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/felipegarcia123/Database-System

2. Create a PostgreSQL database to store client information. In this case i put name, last_name, age, birtday,gender,id as fields
3. Update the database configuration in the config.py file:
    ```bash
    DATABASE = {
        'host': 'localhost',
        'database': 'your_database_name',
        'user': 'your_username',
        'password': 'your_password'
    }
##Usage
Make sure the PostgreSQL database is running before executing the application.

To run the application, use the following command:

    
    python main.py

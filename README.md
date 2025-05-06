# Database-Design-Week-8 - Final Project

# 📚 Library Management System

A full-featured **Library Management System** built using:
- **MySQL** – for relational database design
- **FastAPI (Python)** – for building a RESTful CRUD API
- **DrawSQL** – for visual ER Diagram

This system enables librarians and users to manage members, books, authors, categories, loans, and reservations with complete **CRUD functionality**.

---

## Features

- Full **relational database** with proper constraints and relationships
- RESTful API with support for **Create, Read, Update, and Delete** operations
- Interactive API documentation via **Swagger UI**
- Sample data included for quick setup
- Visual **Entity Relationship Diagram (ERD)** included
- Easy setup instructions for developers

---

## Project Structure

Databas-Design-Week-8/

│

├── README.md

├── erd.png # Entity Relationship Diagram (Exported from DrawSQL)

├── library.sql # MySQL schema with DDL & sample DML

│

└── library-api/

├── main.py # FastAPI application with all routes

├── database.py # Database connection setup

├── models.py # Pydantic models for ORM mapping

├── schemas.py # Request/response validation schemas

└── requirements.txt # Python dependencies


---

##  Setup Instructions

### 1. Clone the Repository

git clone https://github.com/gathecha254/Database-Design-Week-8.git
cd Database-Design-Week-8

### 2. Import your schema

mysql -u root -p
CREATE DATABASE library;
exit;

mysql -u root -p library < library.sql


### 3. Install Python dependencies

cd library-api
pip install -r requirements.txt

### 3. Run the FASTAPI Application

uvicorn main:app --reload
cd library-api
pip install -r requirements.txt

Open the interactive API docs in your browser:
> http://localhost:8000/docs

## Supported API Endpoints

| GET | /authors | Get all authors |
| POST | /authors | Add a new author |
| GET | /authors/{id} | Get author by ID |
| PUT | /authors/{id} | Update author by ID |
| DELETE | /authors/{id} | Delete author by ID |

| GET | /categories | Get all categories |
| POST | /categories | Add a new category |
| GET | /categories/{id} | Get category by ID |
| PUT | /categories/{id} | Update category by ID |
| DELETE | /categories/{id} | Delete category by ID |

| GET | /books | Get all books |
| POST | /books | Add a new book |
| GET | /books/{id} | Get book by ID |
| PUT | /books/{id} | Update book by ID |
| DELETE | /books/{id} | Delete book by ID |

| GET | /loans | Get all loans |
| POST | /loans | Create a new loan |
| GET | /loans/{id} | Get loan by ID |
| PUT | /loans/{id} | Update loan by ID |
| DELETE | /loans/{id} | Delete loan by ID |

| GET | /reservations | Get all reservations |
| POST | /reservations | Create a new reservation |
| GET | /reservations/{id} | Get reservation by ID |
| PUT | /reservations/{id} | Update reservation by ID |
| DELETE | /reservations/{id} | Delete reservation by ID |


## ERD Screenshot

![image](https://github.com/user-attachments/assets/ee79bcf7-ba98-4ada-845a-4e501c887a4d)


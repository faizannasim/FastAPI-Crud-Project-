# User Management System

## Project Overview
This is a REST API project built using FastAPI and MySQL with full CRUD (Create, Read, Update, Delete) functionality.

This project allows users to:
- Create user records
- View all users
- View a single user
- Update user details
- Delete users

---

# Tech Stack
- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Uvicorn

---

# Features

## Home Route
GET /

## Get All Users
GET /users

## Get Single User
GET /users/{user_id}

## Create User
POST /users

## Update User
PUT /users/{user_id}

## Delete User
DELETE /users/{user_id}

---

# Project Structure
User Management System/
│── env/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── requirements.txt

---

# Installation Guide

## Step 1: Clone Repository
git clone <your-repository-link>

## Step 2: Create Virtual Environment
python -m venv env

## Step 3: Activate Virtual Environment (Windows)
.\env\Scripts\Activate.ps1

## Step 4: Install Dependencies
pip install -r requirements.txt

---

# Run the Project
uvicorn main:app --reload

---


# Author
Faizan Nasim

---

# Note
This project was built to strengthen backend development skills and understand real-world API structure using FastAPI.

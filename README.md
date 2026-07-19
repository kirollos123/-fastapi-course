# Python API Development with FastAPI

A production-ready REST API built with **FastAPI** following modern backend development best practices. This project covers the complete lifecycle of developing, testing, containerizing, and deploying a scalable API using Python.

> **Note:** This project was implemented while following the comprehensive *Python API Development* course by Sanjeev Thiyagarajan (freeCodeCamp), with the goal of understanding professional backend development practices and building a production-ready API.

---

# Features

* RESTful API Design
* CRUD Operations
* Request & Response Validation using Pydantic
* PostgreSQL Database Integration
* SQLAlchemy ORM
* JWT Authentication
* OAuth2 Password Flow
* Password Hashing
* User Registration & Login
* Protected Routes
* Authorization (Users can only modify their own resources)
* SQL Relationships
* Voting (Like) System
* Environment Variables
* Alembic Database Migrations
* Docker & Docker Compose
* Automated Testing with Pytest
* CI/CD Pipeline using GitHub Actions
* Production Deployment
* Nginx Reverse Proxy
* Gunicorn Application Server
* HTTPS / SSL Configuration

---

# Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Database

* PostgreSQL
* SQLAlchemy
* Alembic

### Authentication

* JWT
* OAuth2
* Passlib (Password Hashing)

### Testing

* Pytest
* FastAPI TestClient

### DevOps

* Docker
* Docker Compose
* Git
* GitHub Actions
* Gunicorn
* Nginx

---

# Project Structure

```
app/
├── routers/
├── models/
├── schemas/
├── database.py
├── oauth2.py
├── utils.py
├── config.py
├── main.py

alembic/

tests/

Dockerfile

docker-compose.yml

requirements.txt
```

---

# Main Functionalities

## Authentication

* Register new users
* Login
* JWT Access Tokens
* Secure Password Hashing
* Protected Endpoints

---

## Posts

* Create Posts
* Retrieve All Posts
* Retrieve Single Post
* Update Posts
* Delete Posts

---

## Users

* Create User
* Get User Information

---

## Voting

Users can vote (like) posts.

Each user can:

* Vote once
* Remove vote
* Prevent duplicate votes

---

## Database

* PostgreSQL
* SQLAlchemy ORM
* Relationships
* Foreign Keys
* Alembic Migrations

---

# Testing

The project contains automated tests covering:

* Authentication
* User Registration
* CRUD Operations
* Authorization
* Database Fixtures
* Token Validation

Built using:

* Pytest
* FastAPI TestClient

---

# Docker

Containerized application using:

* Dockerfile
* Docker Compose

Includes:

* API Container
* PostgreSQL Container

---

# CI/CD

GitHub Actions pipeline performs:

* Install Dependencies
* Run Pytest
* Build Docker Image
* Validate Deployment Pipeline

---

# Production Deployment

The project demonstrates deployment using:

* Ubuntu Server
* Gunicorn
* Nginx
* HTTPS
* Environment Variables
* PostgreSQL

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Available endpoints:

* Swagger UI (`/docs`)
* ReDoc (`/redoc`)

---

# Learning Outcomes

Through this project I gained hands-on experience with:

* Designing REST APIs
* FastAPI Development
* API Validation
* Authentication & Authorization
* Database Design
* ORM Concepts
* SQL Queries
* Alembic Migrations
* Docker
* Automated Testing
* CI/CD Pipelines
* Production Deployment
* Backend Project Structure
* Environment Configuration
* Secure API Development

---

# Future Improvements

* Refresh Tokens
* Rate Limiting
* Email Verification
* Password Reset
* API Versioning
* Logging
* Monitoring
* Redis Caching
* Pagination Improvements
* Role-Based Access Control (RBAC)

---

# Acknowledgment

This project was built while following the **Python API Development** course by **Sanjeev Thiyagarajan** on **freeCodeCamp** as a learning project to practice professional backend development concepts.

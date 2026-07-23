# Python API Development with FastAPI

A backend REST API built with **FastAPI** as part of my journey to learn modern backend development. This project follows industry best practices while covering the complete lifecycle of API development, from building endpoints to database integration, authentication, testing, containerization, CI/CD, and deployment.

> **Note:** This project is being developed while following the **Python API Development** course by **Sanjeev Thiyagarajan (freeCodeCamp)**. The goal is to gain hands-on experience building production-ready backend applications and understanding professional backend architecture.

---

# Project Goals

- Learn REST API development with FastAPI.
- Understand API design principles.
- Build a scalable backend application.
- Practice database design using PostgreSQL.
- Learn authentication and authorization.
- Apply testing, Docker, CI/CD, and deployment best practices.

---

# Features

## API

- RESTful API Design
- CRUD Operations
- Request Validation
- Response Models
- Status Codes
- Automatic API Documentation

## Database

- PostgreSQL
- SQLAlchemy ORM
- Database Relationships
- Foreign Keys
- Alembic Migrations

## Authentication

- User Registration
- Login
- JWT Authentication
- OAuth2 Password Flow
- Password Hashing
- Protected Routes
- Authorization

## Posts

- Create Posts
- Retrieve Posts
- Retrieve Single Post
- Update Posts
- Delete Posts

## Users

- Register User
- Get User Profile

## Voting

- Like / Vote System
- Prevent Duplicate Votes
- Remove Votes

## DevOps

- Environment Variables
- Docker
- Docker Compose
- Gunicorn
- Nginx
- GitHub Actions
- CI/CD Pipeline

## Testing

- Pytest
- FastAPI TestClient
- Authentication Tests
- CRUD Tests
- Database Fixtures

---

# Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- PostgreSQL
- SQLAlchemy
- Alembic

## Authentication

- JWT
- OAuth2
- Passlib

## Testing

- Pytest
- FastAPI TestClient

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- Gunicorn
- Nginx

---

# Project Structure

```
app/
│
├── routers/
├── models/
├── schemas/
├── database.py
├── oauth2.py
├── config.py
├── utils.py
└── main.py

alembic/

tests/

Dockerfile

docker-compose.yml

requirements.txt
```

---

# API Endpoints

## Posts

- Create Post
- Get All Posts
- Get Single Post
- Update Post
- Delete Post

## Users

- Register User
- Get User

## Authentication

- Login
- Generate JWT Token

## Votes

- Vote on Posts
- Remove Vote

---

# Local Installation

Clone the repository

```bash
git clone https://github.com/kirollos123/Python-API-Development.git
```

Enter the project

```bash
cd Python-API-Development
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

Alternative Documentation

```
http://127.0.0.1:8000/redoc
```

---

# Environment Variables

Create a `.env` file and add:

```env
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=

SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Learning Roadmap

Throughout this project I will practice:

- FastAPI Fundamentals
- HTTP Methods
- Request & Response Validation
- CRUD Operations
- PostgreSQL
- SQLAlchemy ORM
- Pydantic Models
- Authentication
- Authorization
- Relationships
- Alembic
- Docker
- Testing
- CI/CD
- Production Deployment

---

# Future Improvements

- Refresh Tokens
- Email Verification
- Password Reset
- Pagination
- Search & Filtering
- Rate Limiting
- Redis Caching
- Logging
- Monitoring
- Role-Based Access Control (RBAC)

---

# Acknowledgment

This project is based on the **Python API Development – Comprehensive Course for Beginners** by **Sanjeev Thiyagarajan**, published on the **freeCodeCamp.org** YouTube channel.

The implementation in this repository reflects my own learning process while following the course and practicing modern backend development concepts.

---

# Author

**Kirollos Mina**

- GitHub: https://github.com/kirollos123
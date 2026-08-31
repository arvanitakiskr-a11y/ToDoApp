# TodoApp

A RESTful Todo application built with Python and FastAPI.

## Features

* User authentication
* Create, read, update and delete todos
* User management
* Database migrations with Alembic
* API testing with Postman

## Technologies

* Python
* FastAPI
* SQLAlchemy
* Alembic
* SQLite
* Pytest
* Postman

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd TodoApp
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

Then open the API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Database Migrations

Run Alembic migrations with:

```bash
alembic upgrade head
```

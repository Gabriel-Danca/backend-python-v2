# Backend Python - Task API

FastAPI backend for a simple todo list. It exposes CRUD-like operations for tasks using soft delete and includes a health check endpoint.

## Features

- Create a task with default completion/deactivation flags
- Mark a task as completed
- Soft delete a task (set `is_deactivated = true`)
- List active tasks (`is_deactivated = false`)
- Health check endpoint

## Tech Stack

- Python 3.12
- FastAPI 0.109+
- Poetry (Dependency Manager)
- PostgreSQL
- Gunicorn 
- SQLAlchemy 
- Alembic (Database Migrations)
- Pydantic (Data Validation)

## Run Locally


Set DB_URL in an .env file


Ensure you have Poetry installed. If not:

```bash
sudo apt install python3-poetry
```

Install dependencies:

```bash
poetry install
```


# Backend Python - Task API

FastAPI backend for a simple todo list.
It exposes CRUD-like operations for tasks using soft delete and includes a
health check endpoint.

## Features

- Create a task with default completion/deactivation flags
- Mark a task as completed
- Soft delete a task (set `is_deactivated = true`)
- List active tasks (`is_deactivated = false`)
- Health check endpoint
- Database connection check endpoint

## Tech Stack

- Python 3.12
- FastAPI 0.128+
- Poetry (Dependency Manager)
- PostgreSQL
- Uvicorn (ASGI Server)
- SQLAlchemy (ORM)
- Alembic (Database Migrations)

## Development Workflow

Follow these steps to develop locally while running infrastructure in Docker.

### 1. Configure Environment

Ensure you have a `.env` file with the necessary database credentials:
`DATABASE_URL`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.

#### 2. Start Infrastructure

Start PostgreSQL using Docker Compose without running the backend container:

```bash
docker compose up db -d

```

#### 3. Install & Run App Locally

Install dependencies and start the hot-reloading development server:

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

*The app will be available at <http://localhost:8000>*

## Run via Docker (Production Check)

Use this command only to verify the final build or run the full stack in isolation.

```bash
docker compose up --build -d
```

## Architecture Diagram

```text
Client
  |
  v
Router (FastAPI Endpoints)
  |
  v
CRUD (Business Logic)
  |
  v
Session (SQLAlchemy)
  |
  v
PostgreSQL
```

## Configuration

Environment variables used by the app (defined in .env):

- DATABASE_URL (example: postgresql+psycopg://user:pass@localhost:5432/todo_db)

- DB_USER

- DB_PASSWORD

- DB_NAME

Database container variables (used by docker-compose.yml):

- POSTGRES_USER

- POSTGRES_PASSWORD

- POSTGRES_DB

## Tools and What They Do

- FastAPI: Modern, fast web framework for building APIs with Python 3.12+.

- SQLAlchemy: The Python SQL Toolkit and Object Relational Mapper.

- Alembic: Lightweight database migration tool for usage with SQLAlchemy.

- Pydantic: Data validation and settings management using python type annotations.

- Uvicorn: A lightning-fast ASGI server implementation.

- Gunicorn: Production-grade WSGI server used as a process manager to run
            Uvicorn workers.

- Poetry: Tool for dependency management and packaging in Python.

- Pytest: Framework that makes building simple and scalable tests easy.

## Project Object Types

- Request Model (TaskCreateRequest): Input payloads validated by the API.

- Response Model (TaskResponse): Output payloads returned to clients.

- Entity (Task): SQLAlchemy-mapped database model.

- Router: FastAPI endpoints handling request/response orchestration.

- Session: Database session management for transactions.

## Security and Configurations

- Database Connection: Configured via pydantic-settings using
                       DATABASE_URL from the environment.

- Validation: Strict typing and validation via Pydantic models.

- Logging: Configured to output INFO level logs to stdout.

## API Endpoints

- GET /api/tasks - List all active tasks

- POST /api/tasks - Create a new task

- PATCH /api/tasks/{id}/complete - Mark a task as completed

- DELETE /api/tasks/{id} - Soft delete a task

- GET /health - Application health check

- GET /db-check - Verify database connectivity

## Logging

Uses the standard Python logging module.
Log statements are added in the controller layer for key operations.

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
```

## Example Payload

Create Task (POST /api/tasks)

```json
{
  "task": "Buy groceries",
  "is_completed": false,
  "is_deactivated": false
}
```

For this backend, we are going to use the following tools:
- FastAPI 
- PostgreSQL
- Poetry
- SQLAlchemy + psycopg 
- Alembic
- Uvicorn / Gunicorn
- Docker / Docker compose

The following commands were verified on a Linux system as of January 19, 2026. Please note that tools and best practices evolve over time. If you encounter issues, refer to the official documentation for each tool (links provided) to adapt to any changes.

Poetry: https://python-poetry.org/docs/
(To continue)

If you don't have Poetry installed, please run the following command:

```bash
sudo apt install python3-poetry
```

Install all necessary dependencies for the project:

```bash
poetry install
```

To run the database, run the following:
```bash
docker compose up -d
```

Initialize Alembic:
```bash
poetry run alembic upgrade head
```

To run the server, use the following:
```bash
poetry run uvicorn app.main:app 
```
<!-- poetry run gunicorn -k uvicorn.workers.UvicornWorker -w 1 -b 127.0.0.1:8000 app.main:app -->

Test the endpoints:
```bash
curl http://127.0.0.1:8000/health 
(should return "status": "ok")

curl http://127.0.0.1:8000/db-check
(should return "db": 1)
```
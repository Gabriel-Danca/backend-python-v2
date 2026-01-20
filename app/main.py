from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine


app = FastAPI(title="python-backend-gdanca")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        value = conn.execute(text("select 1")).scalar_one()
    return {"db": value}

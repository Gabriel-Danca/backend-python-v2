from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.session import SessionLocal
from app.models import Task
from app import schemas
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Python Backend", version="1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/tasks", response_model=schemas.TaskResponse, tags=["task-controller"], summary="Create task")
def create_task(task_data: schemas.TaskCreateRequest, db: Session = Depends(get_db)):
    logger.info(f"Creating new task: {task_data.task}")
    
    new_task = Task(
        task=task_data.task,
        is_completed=task_data.is_completed,
        is_deactivated=task_data.is_deactivated
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    logger.info(f"Task created with ID: {new_task.id}")
    return new_task

@app.get("/api/tasks", response_model=list[schemas.TaskResponse], tags=["task-controller"], summary="List active tasks")
def get_active_tasks(db: Session = Depends(get_db)):
    logger.info("Reading active tasks list")
    stmt = select(Task).where(Task.is_deactivated == False)
    tasks = db.execute(stmt).scalars().all()
    return tasks

@app.patch("/api/tasks/{id}/complete", response_model=schemas.TaskResponse, tags=["task-controller"], summary="Mark task completed")
def mark_completed(id: int, db: Session = Depends(get_db)):
    logger.info(f"Request to mark task {id} as completed")
    
    db_task = db.get(Task, id)
    if not db_task:
        logger.warning(f"Task {id} not found")
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_task.is_completed = True
    db.commit()
    db.refresh(db_task)
    
    return db_task


@app.delete("/api/tasks/{id}", response_model=schemas.TaskResponse, tags=["task-controller"], summary="Deactivate task")
def deactivate_task(id: int, db: Session = Depends(get_db)):
    logger.info(f"Request to deactivate task {id}")
    
    db_task = db.get(Task, id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db_task.is_deactivated = True
    db.commit()
    db.refresh(db_task) 
    
    return db_task


@app.get("/health", tags=["health-controller"], summary="Application health check")
def health():
    logger.debug("Health check probe received")
    return {"status": "ok"}

@app.get("/db-check", tags=["health-controller"], summary="Database Connection Check")
def db_check(db: Session = Depends(get_db)):
    try:
        db.execute(select(1))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail=f"Database connection failed: {str(e)}"
        )
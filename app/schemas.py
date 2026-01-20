from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True
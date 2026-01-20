from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskBase(BaseModel):
    task: str
    is_completed: bool = False
    is_deactivated: bool = False

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel, Field, ConfigDict

class TaskBase(BaseModel):
    task: str = Field(..., max_length=500, min_length=0, description="Task description")
    is_completed: bool = False
    is_deactivated: bool = False

class TaskCreateRequest(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
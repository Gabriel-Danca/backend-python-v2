from pydantic import BaseModel, ConfigDict, Field, computed_field
from datetime import datetime

class TaskCreateRequest(BaseModel):
    task: str
    is_completed: bool = False
    is_deactivated: bool = False

class TaskResponse(BaseModel):
    id: int
    task: str
    is_completed: bool
    is_deactivated: bool
    created_at: datetime
    updated_at: datetime

    @computed_field
    def completed(self) -> bool:
        return self.is_completed

    @computed_field
    def deactivated(self) -> bool:
        return self.is_deactivated

    model_config = ConfigDict(from_attributes=True)
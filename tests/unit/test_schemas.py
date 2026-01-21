from datetime import datetime
from app.schemas import TaskResponse

def test_task_response_compatibility_logic():
    mock_data = {
        "id": 1,
        "task": "Test Unit",
        "is_completed": True,     
        "is_deactivated": False, 
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    task_schema = TaskResponse(**mock_data)

    assert task_schema.completed is True 
    assert task_schema.completed == task_schema.is_completed
    
    assert task_schema.deactivated is False
    assert task_schema.deactivated == task_schema.is_deactivated

def test_task_response_types():

    mock_data = {
        "id": 1,
        "task": "Test Types",
        "is_completed": False,
        "is_deactivated": False,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    task = TaskResponse(**mock_data)
    assert isinstance(task.task, str)
    assert isinstance(task.id, int)
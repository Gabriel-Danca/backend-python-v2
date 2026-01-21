from datetime import datetime
from app.schemas import TaskCreateRequest, TaskResponse

def test_task_create_schema():
    req = TaskCreateRequest(task="Test Task")
    assert req.task == "Test Task"
    assert req.is_completed is False
    assert req.is_deactivated is False

def test_task_response_model():
    mock_data = {
        "id": 1,
        "task": "Test Unit",
        "is_completed": True,
        "is_deactivated": False,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    
    task_schema = TaskResponse(**mock_data)
    
    assert task_schema.id == 1
    assert task_schema.task == "Test Unit"
    assert task_schema.is_completed is True
    
    try:
        assert task_schema.completed
        assert False, "Should not have 'completed' attribute"
    except AttributeError:
        assert True
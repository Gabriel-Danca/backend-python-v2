from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import schemas

def test_integration(client: TestClient):
    task_payload = {
        "task": "Integration Test Task",
        "is_completed": False,
        "is_deactivated": False
    }
    
    response = client.post("/api/tasks", json=task_payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "Integration Test Task"
    assert "id" in data
    
    task_id = data["id"]

    response = client.get("/api/tasks")
    assert response.status_code == 200
    tasks = response.json()
    
    found_task = next((t for t in tasks if t["id"] == task_id), None)
    assert found_task is not None
    assert found_task["task"] == "Integration Test Task"
    assert found_task["completed"] is False  

    response = client.patch(f"/api/tasks/{task_id}/complete")
    assert response.status_code == 200
    
    updated_data = response.json()
    assert updated_data["is_completed"] is True
    assert updated_data["completed"] is True

    response = client.get("/api/tasks")
    tasks = response.json()
    found_task = next((t for t in tasks if t["id"] == task_id), None)
    assert found_task["is_completed"] is True

    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    
    deleted_data = response.json()
    assert deleted_data["is_deactivated"] is True
    assert deleted_data["deactivated"] is True

    response = client.get("/api/tasks")
    tasks = response.json()
    
    found_task = next((t for t in tasks if t["id"] == task_id), None)
    assert found_task is None
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
    
    assert found_task["is_completed"] is False
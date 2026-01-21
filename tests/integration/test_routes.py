def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={"task": "Buy groceries", "is_completed": False}
    )
    assert response.status_code == 200 
    data = response.json()
    assert data["task"] == "Buy groceries"
    assert data["is_completed"] is False
    assert "id" in data

def test_read_tasks(client):
    client.post("/api/tasks", json={"task": "Walk the dog"})
    
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_complete_task(client):
    res_create = client.post("/api/tasks", json={"task": "Task to complete"})
    task_id = res_create.json()["id"]
    
    response = client.patch(f"/api/tasks/{task_id}/complete")
    
    assert response.status_code == 200
    data = response.json()
    assert data["is_completed"] is True
    assert data["completed"] is True 

def test_delete_task(client):
    res_create = client.post("/api/tasks", json={"task": "Task to delete"})
    task_id = res_create.json()["id"]
    
    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 200 
    
    assert response.json()["is_deactivated"] is True
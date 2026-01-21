def test_create_task(client):
    response = client.post("/api/tasks", json={"task": "Buy milk"})
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "Buy milk"
    assert "id" in data
    assert data["is_completed"] is False

def test_read_tasks(client):
    client.post("/api/tasks", json={"task": "Task to read"})
    
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_complete_task(client):
    res_create = client.post("/api/tasks", json={"task": "Task to complete"})
    task_id = res_create.json()["id"]
    
    response = client.patch(f"/api/tasks/{task_id}/complete")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["is_completed"] is True

def test_delete_task(client):
    res_create = client.post("/api/tasks", json={"task": "Task to delete"})
    task_id = res_create.json()["id"]
    
    response = client.delete(f"/api/tasks/{task_id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["is_deactivated"] is True
    
    res_list = client.get("/api/tasks")
    tasks = res_list.json()
    assert not any(t["id"] == task_id for t in tasks)
def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={"task": "Buy groceries", "is_completed": False}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["task"] == "Buy groceries"
    assert data["is_completed"] is False
    assert "id" in data

def test_read_tasks(client):
    client.post("/tasks/", json={"task": "Walk the dog"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_task(client):
    res_create = client.post("/tasks/", json={"task": "Old Task"})
    task_id = res_create.json()["id"]
    
    response = client.put(
        f"/tasks/{task_id}",
        json={"task": "New Task", "is_completed": True, "is_deactivated": False}
    )
    assert response.status_code == 200
    assert response.json()["task"] == "New Task"
    assert response.json()["is_completed"] is True

def test_delete_task(client):
    res_create = client.post("/tasks/", json={"task": "Task to delete"})
    task_id = res_create.json()["id"]
    
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={"name": "Unit Testing"}
    )
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "Unit Testing"
    assert "id" in data

def test_read_tasks(client):
    client.post("/tasks/", json={"name": "Task"})
    
    response = client.get("/tasks/")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[-1]["name"] == "Task"

def test_update_task(client):
    res_create = client.post("/tasks/", json={"name": "old task"})
    task_id = res_create.json()["id"]
    
    response = client.put(
        f"/tasks/{task_id}",
        json={"name": "new task"}
    )
    
    assert response.status_code == 200
    assert response.json()["name"] == "new task"

def test_delete_task(client):
    res_create = client.post("/tasks/", json={"name": "temp task"})
    task_id = res_create.json()["id"]
    
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    res_get = client.get(f"/tasks/{task_id}")
    assert res_get.status_code == 404
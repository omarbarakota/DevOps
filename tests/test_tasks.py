
import pytest
from flask import Flask
from datetime import datetime
from main import app, tasks

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    initial_task_count = len(tasks)
    new_task = 'New Task'
    response = client.post('/add_task', data={'task': new_task}, follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == initial_task_count + 1 #Check no of task + the already created in the test
    assert new_task in tasks    #Make sure that new task is added
    assert new_task in response.data.decode('utf-8')

def test_delete_task(client):
    initial_task_count = len(tasks)
    task_to_delete = 0  # Index of the task to delete
    response = client.post(f'/delete_task/{task_to_delete}', follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == initial_task_count - 1 #Check no of task - the already deleted in the test
    assert 'New Task' not in tasks              #check if the deleted task still exists
    assert 'New Task' not in response.data.decode('utf-8')

#test_add_task(app.test_client())
#test_delete_task(app.test_client())
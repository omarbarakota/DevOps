import pytest
from flask import Flask
from datetime import datetime
from main import app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    current_time = datetime.now().strftime('%Y-%B-%d \n%I:%M-%p')
    assert current_time in response.data.decode('utf-8')

#test_index(app.test_client())

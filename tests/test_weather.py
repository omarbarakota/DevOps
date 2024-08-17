import pytest
from flask import Flask
from unittest.mock import patch,MagicMock
#import requests
from main import app

mock_get=MagicMock()

@pytest.fixture

def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_weather_valid_city(client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'name': 'Cairo',
        'main': {'temp': 25},
        'weather': [{'description': 'clear sky'}]
    }
    response = client.post('/weather', data={'city': 'Cairo'})
    assert response.status_code == 200
    assert 'Cairo' in response.data.decode('utf-8')
    

#@patch('requests.get')
# def test_weather_invalid_city(client):
#     mock_get.return_value.status_code = 404
#     response = client.post('/weather', data={'city': 'InvalidCity'})
#     assert response.status_code == 200
#     assert 'City not found' in response.data.decode('utf-8')

# def test_weather_no_city(client):
#     response = client.post('/weather', data={'city': ''})
#     assert response.status_code == 200
#     assert 'City name is required' in response.data.decode('utf-8')


import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_valid_data(client):
    response = client.post('/registration', data={
        'email': 'user@example.com',
        'phone': '1234567890',
        'name': 'John',
        'address': '123 Main',
        'index': '123456',
        'comment': 'Test comment'
    })
    assert b'Success!' in response.data

def test_invalid_email(client):
    response = client.post('/registration', data={
        'email': 'user@invalid',
        'phone': '1234567890',
        'name': 'John',
        'address': '123 Main',
        'index': '123456'
    })
    assert b'Invalid email format' in response.data

def test_short_phone(client):
    response = client.post('/registration', data={
        'email': 'user@example.com',
        'phone': '123',
        'name': 'John',
        'address': '123 Main',
        'index': '123456'
    })
    assert b'Phone must be exactly 10 digits' in response.data

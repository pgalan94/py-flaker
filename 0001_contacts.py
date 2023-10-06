from app import app
import pytest

# Create a test client for the Flask app
@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# Test the root endpoint
def test_root_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert '/api/contacts' in data['results']

# Test the GET method for /api/contacts
def test_get_contacts(client):
    response = client.get('/api/contacts')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'results' in data

# Test the POST method for /api/contacts
def test_post_contact(client):
    data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '123-456-7890'
    }
    response = client.post('/api/contacts', data=data)
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Contact created successfully'

# Test pagination parameters for /api/contacts
def test_pagination(client):
    response = client.get('/api/contacts?page=1&limit=10')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'results' in data
    assert 'next' in data
    assert 'prev' in data

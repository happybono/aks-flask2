import pytest
import app as myapp

@pytest.fixture
def app():
    return myapp.app

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

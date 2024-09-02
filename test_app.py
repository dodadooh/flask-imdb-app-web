import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_list(client):
    rv = client.get('/get-list')
    assert rv.status_code == 200
    # Expecting an empty list, as per current test output
    assert rv.json == []



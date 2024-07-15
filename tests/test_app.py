import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_main_page(client):
    rv = client.get('/')
    assert b'Hello, World!' in rv.data
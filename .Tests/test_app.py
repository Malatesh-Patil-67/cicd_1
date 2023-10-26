import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_page(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data

def test_stock_data_submission(client):
    response = client.post('/', data={'stock_symbol': 'AAPL'})
    assert b'AAPL' in response.data

def test_stock_data_plot(client):
    response = client.post('/', data={'stock_symbol': 'AAPL'})
    assert b'Price' in response.data  # Check for the 'Price' label on the plot image.

def test_example():
    assert 1 == 1

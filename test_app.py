import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_page(client):
    response = client.get('/')
   
    assert b"Enter Stock Symbol:" in response.data

def test_stock_data_submission(client):
    response = client.post('/', data={'stock_symbol': 'AAPL'})
    assert b"AAPL" in response.data

def test_stock_data_plot(client):
    response = client.post('/', data={'stock_symbol': 'AAPL'})
    assert b"Stock Symbol:" in response.data
 # Adjust this text according to your "home.html" template

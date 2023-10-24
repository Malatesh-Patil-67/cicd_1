# test_app.py

from app import app
import pytest
from flask import Flask

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_home_page(client):
    response = client.get('/')
    assert b'Welcome to My Flask App' in response.data

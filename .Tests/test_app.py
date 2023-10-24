import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # This adds the parent directory to sys.path

from app import app  # Now, you should be able to import app
import pytest
from flask import Flask

# ...rest of your test code

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_page(client):
    response = client.get('/')
    assert b'Welcome to My Flask App' in response.data

def test_example():
    assert 1 == 1

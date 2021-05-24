import json
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
  response = client.get('/')
  assert json.loads(response.content) == {'message': 'Server is Running'}
  assert response.status_code == 200
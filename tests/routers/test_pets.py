import json
from pathlib import Path
from unittest.mock import patch
from main import app
from database import repository

from fastapi.testclient import TestClient

client = TestClient(app)
mock_data_base = Path("tests", "mock")


def test_get_pets():
  pets = json.load((mock_data_base / "pets.json").open())
  with patch.object(repository, 'get_pets', return_value=pets):
    response = client.get('/pets')
    assert json.loads(response.content) == pets
    assert response.status_code == 200


def test_get_pet():
  pet = json.load((mock_data_base / "pet.json").open())
  with patch.object(repository, 'get_pet', return_value=pet):
    response = client.get('/pets/1')
    assert json.loads(response.content) == pet
    assert response.status_code == 200


def test_create_pet():
  pet = json.load((mock_data_base / "pet.json").open())
  with patch.object(repository, 'create_pet', return_value=pet):
    response = client.post('/pets', json=pet)
    assert json.loads(response.content) == pet
    assert response.status_code == 201


def test_delete_pet():
  with patch.object(repository, 'get_pets', return_value=1):
    response = client.delete('/pets/1')
    assert json.loads(response.content) == {'message': 'Successfully deleted pet ID 1'}
    assert response.status_code == 200
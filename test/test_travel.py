import os
os.environ["ENV"] = "test"
import pytest
from fastapi.testclient import TestClient
from app.main import app
from database import Base, engine

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

def test_create_travel():
    res = client.post("/travels/", params={"code": "Abc123",
    "travel_from": "Oaxaca",
    "travel_to": "Puebla",            
    "departure_date": "2023-01-01 10:00"})
    assert res.status_code == 200
    data = res.json()
    assert data["code"] == "Abc123"
    assert data["travel_from"] == "Oaxaca"

def test_get_travel():
    client.post("/travels/", params={"code": "Abc123",
    "travel_from": "Oaxaca",
    "travel_to": "Puebla",            
    "departure_date": "2023-01-01 10:00"})
    res = client.get("/travels/1")
    assert res.status_code == 200
    data = res.json()
    assert data["nombre"] == "Ana"

def test_not_found_travel():
    res = client.get("/travels/999")
    assert res.status_code == 404

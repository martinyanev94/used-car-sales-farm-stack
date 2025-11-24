from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "test_user", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"username": "test_user", "email": "test@example.com"}

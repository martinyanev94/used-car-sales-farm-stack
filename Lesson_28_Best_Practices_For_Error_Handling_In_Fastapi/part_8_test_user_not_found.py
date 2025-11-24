from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

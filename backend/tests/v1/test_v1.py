from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/v1/items",
        json={"name": "test", "description": "test description"},
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "test",
                               "description": "test description"}

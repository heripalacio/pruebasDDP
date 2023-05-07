from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_is_prime():
    response = client.get("/IsPrime/1")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}
    response = client.get("/IsPrime/2")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}
    response = client.get("/IsPrime/3")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}
    response = client.get("/IsPrime/4")
    assert response.status_code == 200
    assert response

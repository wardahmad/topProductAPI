from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_top_product():
    response = client.get("/topProduct")
    assert response.status_code == 415
    assert response.json() == {"detail": "Unsupported Media Type"}

# def test_top_product():
#     response = client.get("/topProduct")
#     assert response.status_code == 200
#     # assert response.json() == {"detail": ""}
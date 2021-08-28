from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# def test_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World"}

# in main.py, When Uncomment this variable ( csv File Path = '.\data.mp3 ), we'll return passed'
# def test_top_product():
#     response = client.get("/topProduct")
#     assert response.status_code == 415
#     assert response.json() == {"detail": "Unsupported Media Type"}

# I Need to create a Variable for this function, to test function outputs


def test_top_product():
    response = client.get("/topProduct")
    assert response.status_code == 200
    assert response.json() == {
        "top_product": "ice cream card",
        "product_rating": 5.1}

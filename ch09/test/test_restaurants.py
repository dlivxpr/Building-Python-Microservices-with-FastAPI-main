from api import restaurant
from fastapi.testclient import TestClient

client = TestClient(restaurant.router)

def test_restaurant_index():
    response = client.get("/restaurant/index")
    assert response.status_code == 200
    assert response.text == "The Restaurants"

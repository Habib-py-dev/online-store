# tests/test_products.py
# Unit tests for product endpoints

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_products():
    """Test creating a product via POST request."""
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 20


def test_create_product():
    """Create a new product in the database."""
    new_product = {
        "id": 23,
        "name": "Test Product",
        "price": 9.99,
        "stock": 5,
        "category": "Test"
    }
    response = client.post("/products", json=new_product)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"

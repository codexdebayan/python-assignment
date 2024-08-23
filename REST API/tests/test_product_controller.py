import pytest
from flask import Flask
from app.controllers.product_controller import ProductController

@pytest.fixture
def client():
    app = Flask(__name__)
    app.add_url_rule('/products', view_func=ProductController.get_all_products)
    app.add_url_rule('/products/<product_id>', view_func=ProductController.get_product_by_id)
    app.add_url_rule('/products', methods=['POST'], view_func=ProductController.create_product)
    app.add_url_rule('/products/<product_id>', methods=['PUT'], view_func=ProductController.update_product)
    app.add_url_rule('/products/<product_id>', methods=['DELETE'], view_func=ProductController.delete_product)
    return app.test_client()

def test_get_all_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert 'application/json' in response.content_type

def test_get_product_by_id(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    assert 'application/json' in response.content_type

def test_create_product(client):
    data = {
        'ProductID': 99999,
        'ProductName': 'New Product',
        'SupplierID': 1,
        'CategoryID': 1,
        'QuantityPerUnit': '10 boxes',
        'UnitPrice': 20.00,
        'UnitsInStock': 100,
        'UnitsOnOrder': 0,
        'ReorderLevel': 10,
        'Discontinued': False
    }
    response = client.post('/products', json=data)
    assert response.status_code == 201
    assert response.json['ProductID'] == 99999

def test_update_product(client):
    # Ensure the product exists or set it up
    initial_data = {
        'ProductName': 'Initial Product',
        'ProductID': 1
    }
    client.post('/products', json=initial_data)  # Create initial product

    # Prepare the update data
    data = {
        'ProductName': 'Updated Product'
    }

    # Perform the PUT request to update the product
    response = client.put('/products/1', json=data)

    # Verify the response
    assert response.status_code == 200
    assert response.json['ProductName'] == 'Updated Product'


def test_delete_product(client):
    response = client.delete('/products/99999')
    assert response.status_code == 200
    assert response.json['message'] == 'Product deleted successfully'
from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Paths to the CSV files
CSV_FILE_PATH_CUSTOMERS = 'Northwind_database_csv/customers.csv'
CSV_FILE_PATH_PRODUCTS = 'Northwind_database_csv/products.csv'
CSV_FILE_PATH_ORDERS = 'Northwind_database_csv/orders.csv'

# Helper function to load CSV into a DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)

# Helper function to save the DataFrame back to the CSV
def save_data(df, file_path):
    df.to_csv(file_path, index=False)

# Customers Endpoints
@app.route('/customers', methods=['GET'])
def get_customers():
    df = load_data(CSV_FILE_PATH_CUSTOMERS)
    return jsonify(df.to_dict(orient='records'))

@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    df = load_data(CSV_FILE_PATH_CUSTOMERS)
    customer = df[df['CustomerID'] == customer_id]
    if customer.empty:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify(customer.to_dict(orient='records')[0])

@app.route('/customers', methods=['POST'])
def add_customer():
    new_customer = request.json
    df = load_data(CSV_FILE_PATH_CUSTOMERS)
    if df[df['CustomerID'] == new_customer['CustomerID']].empty:
        df = df.append(new_customer, ignore_index=True)
        save_data(df, CSV_FILE_PATH_CUSTOMERS)
        return jsonify(new_customer), 201
    else:
        return jsonify({'error': 'Customer already exists'}), 400

@app.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    updated_data = request.json
    df = load_data(CSV_FILE_PATH_CUSTOMERS)
    if df[df['CustomerID'] == customer_id].empty:
        return jsonify({'error': 'Customer not found'}), 404
    df.update(pd.DataFrame([updated_data]))
    save_data(df, CSV_FILE_PATH_CUSTOMERS)
    return jsonify(updated_data)

@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    df = load_data(CSV_FILE_PATH_CUSTOMERS)
    if df[df['CustomerID'] == customer_id].empty:
        return jsonify({'error': 'Customer not found'}), 404
    df = df[df['CustomerID'] != customer_id]
    save_data(df, CSV_FILE_PATH_CUSTOMERS)
    return jsonify({'message': 'Customer deleted'})

# Products Endpoints
@app.route('/products', methods=['GET'])
def get_products():
    df = load_data(CSV_FILE_PATH_PRODUCTS)
    return jsonify(df.to_dict(orient='records'))

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    df = load_data(CSV_FILE_PATH_PRODUCTS)
    product = df[df['ProductID'] == int(product_id)]
    if product.empty:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.to_dict(orient='records')[0])

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    df = load_data(CSV_FILE_PATH_PRODUCTS)
    if df[df['ProductID'] == new_product['ProductID']].empty:
        df = df.append(new_product, ignore_index=True)
        save_data(df, CSV_FILE_PATH_PRODUCTS)
        return jsonify(new_product), 201
    else:
        return jsonify({'error': 'Product already exists'}), 400

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    updated_data = request.json
    df = load_data(CSV_FILE_PATH_PRODUCTS)
    if df[df['ProductID'] == int(product_id)].empty:
        return jsonify({'error': 'Product not found'}), 404
    df.update(pd.DataFrame([updated_data]))
    save_data(df, CSV_FILE_PATH_PRODUCTS)
    return jsonify(updated_data)

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    df = load_data(CSV_FILE_PATH_PRODUCTS)
    if df[df['ProductID'] == int(product_id)].empty:
        return jsonify({'error': 'Product not found'}), 404
    df = df[df['ProductID'] != int(product_id)]
    save_data(df, CSV_FILE_PATH_PRODUCTS)
    return jsonify({'message': 'Product deleted'})

# Orders Endpoints
@app.route('/orders', methods=['GET'])
def get_orders():
    df = load_data(CSV_FILE_PATH_ORDERS)
    return jsonify(df.to_dict(orient='records'))

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    df = load_data(CSV_FILE_PATH_ORDERS)
    order = df[df['OrderID'] == int(order_id)]
    if order.empty:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order.to_dict(orient='records')[0])

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.json
    df = load_data(CSV_FILE_PATH_ORDERS)
    if df[df['OrderID'] == new_order['OrderID']].empty:
        df = df.append(new_order, ignore_index=True)
        save_data(df, CSV_FILE_PATH_ORDERS)
        return jsonify(new_order), 201
    else:
        return jsonify({'error': 'Order already exists'}), 400

@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    updated_data = request.json
    df = load_data(CSV_FILE_PATH_ORDERS)
    if df[df['OrderID'] == int(order_id)].empty:
        return jsonify({'error': 'Order not found'}), 404
    df.update(pd.DataFrame([updated_data]))
    save_data(df, CSV_FILE_PATH_ORDERS)
    return jsonify(updated_data)

@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    df = load_data(CSV_FILE_PATH_ORDERS)
    if df[df['OrderID'] == int(order_id)].empty:
        return jsonify({'error': 'Order not found'}), 404
    df = df[df['OrderID'] != int(order_id)]
    save_data(df, CSV_FILE_PATH_ORDERS)
    return jsonify({'message': 'Order deleted'})

# Order History Endpoint
@app.route('/customers/<customer_id>/orders', methods=['GET'])
def get_customer_orders(customer_id):
    df_orders = load_data(CSV_FILE_PATH_ORDERS)
    customer_orders = df_orders[df_orders['CustomerID'] == customer_id]
    
    if customer_orders.empty:
        return jsonify({'error': 'No orders found for this customer'}), 404
    
    return jsonify(customer_orders.to_dict(orient='records'))

if __name__ == '__main__':
    # Create CSV files with headers if they do not exist
    if not os.path.exists(CSV_FILE_PATH_CUSTOMERS):
        pd.DataFrame(columns=['CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax']).to_csv(CSV_FILE_PATH_CUSTOMERS, index=False)

    if not os.path.exists(CSV_FILE_PATH_PRODUCTS):
        pd.DataFrame(columns=['ProductID', 'ProductName', 'SupplierID', 'CategoryID', 'QuantityPerUnit', 'UnitPrice', 'UnitsInStock', 'UnitsOnOrder', 'ReorderLevel', 'Discontinued']).to_csv(CSV_FILE_PATH_PRODUCTS, index=False)

    if not os.path.exists(CSV_FILE_PATH_ORDERS):
        pd.DataFrame(columns=['OrderID', 'CustomerID', 'EmployeeID', 'OrderDate', 'RequiredDate', 'ShippedDate', 'ShipVia', 'Freight', 'ShipName', 'ShipAddress', 'ShipCity', 'ShipRegion', 'ShipPostalCode', 'ShipCountry']).to_csv(CSV_FILE_PATH_ORDERS, index=False)
    
    app.run(debug=True)

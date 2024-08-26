# customer_controller.py

import pandas as pd
from flask import jsonify,request
from app.models.customer_model import CustomerModel
from marshmallow import ValidationError
import logging

class CustomerController:

    @staticmethod
    def get_all_customers():
        # Logic to load all customers from CSV
        df = pd.read_csv('Northwind_database_csv/customers.csv')
        return jsonify(df.to_dict(orient='records'))

    @staticmethod
    def get_customer(customer_id):
        # Logic to load a specific customer from CSV
        df = pd.read_csv('Northwind_database_csv/customers.csv')
        customer = df[df['CustomerID'] == customer_id]
        if customer.empty:
            return jsonify({'error': 'Customer not found'}), 404
        return jsonify(customer.to_dict(orient='records')[0])

    @staticmethod        
    def add_customer():
        json_data=request.get_json()
        try:
            data = CustomerModel.schema.load(json_data)
        except ValidationError as err:
            return jsonify({'errors': err.messages}), 400

        df = CustomerModel.load_data()
        if not df[df['CustomerID'] == data['CustomerID']].empty:
            return jsonify({'error': 'Customer already exists'}), 400

        df = df._append(pd.DataFrame([data]), ignore_index=True)
        CustomerModel.save_data(df)
        return jsonify(data), 201

    

    @staticmethod
    def update_customer(customer_id):
        data = request.json
        df = pd.read_csv('Northwind_database_csv/customers.csv')
        if df[df['CustomerID'] == customer_id].empty:
            return jsonify({'error': 'Customer not found'}), 404
        df.update(pd.DataFrame([data]))
        df.to_csv('Northwind_database_csv/customers.csv', index=False)
        return jsonify(data), 200

    @staticmethod
    def get_customer_orders(customer_id):
        # Logic to get orders for a customer
        df_orders = pd.read_csv('Northwind_database_csv/orders.csv')
        customer_orders = df_orders[df_orders['CustomerID'] == customer_id]
        if customer_orders.empty:
            return jsonify({'error': 'No orders found for this customer'}), 404
        return jsonify(customer_orders.to_dict(orient='records'))

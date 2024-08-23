# customer_controller.py

import pandas as pd
from flask import jsonify,request

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
    # def add_customer(data):
    #     # Logic to add a new customer
    #     df = pd.read_csv('Northwind_database_csv/customers.csv')
    #     if df[df['CustomerID'] == data['CustomerID']].empty:
    #         df = df.append(data, ignore_index=True)
    #         df.to_csv('Northwind_database_csv/customers.csv', index=False)
    #         return jsonify(data), 201
    #     else:
    #         return jsonify({'error': 'Customer already exists'}), 400


    def add_customer(data):
        # Load existing customers from the CSV file
        df = pd.read_csv('Northwind_database_csv/customers.csv')
        
        # Check if the CustomerID already exists
        if df[df['CustomerID'] == data['CustomerID']].empty:
            # Convert the new customer data to a DataFrame
            new_customer_df = pd.DataFrame([data])
            
            # Concatenate the new customer data to the existing DataFrame
            df = pd.concat([df, new_customer_df], ignore_index=True)
            
            # Save the updated DataFrame back to the CSV file
            df.to_csv('Northwind_database_csv/customers.csv', index=False)
            
            return data, 201  # Return the data and a success status code
        else:
            return {'error': 'Customer already exists'}, 400  # Return an error message and a bad request status code

    # def add_customer():
    #     data = request.json
    #     df = pd.read_csv('Northwind_database_csv/customers.csv')
    #     if df[df['CustomerID'] == data['CustomerID']].empty:
    #         new_customer_df = pd.DataFrame([data])
    #         df = pd.concat([df, new_customer_df], ignore_index=True)
    #         df.to_csv('Northwind_database_csv/customers.csv', index=False)
    #         return jsonify(data), 201
    #     else:
    #         return jsonify({'error': 'Customer already exists'}), 400

    @staticmethod
    # def update_customer(customer_id, data):
    #     # Logic to update a customer
    #     df = pd.read_csv('Northwind_database_csv/customers.csv')
    #     if df[df['CustomerID'] == customer_id].empty:
    #         return {'error': 'Customer not found'}, 404
    #     df.update(pd.DataFrame([data]))
    #     df.to_csv('Northwind_database_csv/customers.csv', index=False)
    #     return data, 200

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

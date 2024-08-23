# # app/controllers/order_controller.py
# from flask import jsonify
# from app.models.order_model import OrderModel
# from marshmallow import ValidationError

# class OrderController:
#     @staticmethod
#     def get_all_orders():
#         df = OrderModel.load_data()
#         data = df.to_dict(orient='records')
#         return jsonify(data), 200

#     @staticmethod
#     def get_order_by_id(order_id):
#         df = OrderModel.load_data()
#         order = df[df['OrderID'] == int(order_id)]
#         if order.empty:
#             return jsonify({'error': 'Order not found'}), 404
#         data = order.to_dict(orient='records')[0]
#         return jsonify(data), 200

#     @staticmethod
#     def create_order(json_data):
#         try:
#             data = OrderModel.schema.load(json_data)
#         except ValidationError as err:
#             return jsonify({'errors': err.messages}), 400

#         df = OrderModel.load_data()
#         if not df[df['OrderID'] == data['OrderID']].empty:
#             return jsonify({'error': 'Order already exists'}), 400

#         df = df.append(data, ignore_index=True)
#         OrderModel.save_data(df)
#         return jsonify(data), 201

#     @staticmethod
#     def update_order(order_id, json_data):
#         df = OrderModel.load_data()
#         if df[df['OrderID'] == int(order_id)].empty:
#             return jsonify({'error': 'Order not found'}), 404

#         try:
#             data = OrderModel.schema.load(json_data, partial=True)
#         except ValidationError as err:
#             return jsonify({'errors': err.messages}), 400

#         df.loc[df['OrderID'] == int(order_id), data.keys()] = data.values()
#         OrderModel.save_data(df)
#         updated_order = df[df['OrderID'] == int(order_id)].to_dict(orient='records')[0]
#         return jsonify(updated_order), 200

#     @staticmethod
#     def delete_order(order_id):
#         df = OrderModel.load_data()
#         if df[df['OrderID'] == int(order_id)].empty:
#             return jsonify({'error': 'Order not found'}), 404

#         df = df[df['OrderID'] != int(order_id)]
#         OrderModel.save_data(df)
#         return jsonify({'message': 'Order deleted successfully'}), 200

#     @staticmethod
#     def get_orders_by_customer(customer_id):
#         df = OrderModel.load_data()
#         orders = df[df['CustomerID'] == customer_id]
#         if orders.empty:
#             return jsonify({'error': 'No orders found for this customer'}), 404
#         data = orders.to_dict(orient='records')
#         return jsonify(data), 200


# app/controllers/order_controller.py

import pandas as pd
from flask import jsonify, request
from app.models.order_model import OrderModel
from marshmallow import ValidationError

class OrderController:
    @staticmethod
    def get_all_orders():
        """Retrieve all orders."""
        try:
            df = OrderModel.load_data()
            data = df.to_dict(orient='records')
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_order_by_id(order_id):
        """Retrieve a specific order by ID."""
        try:
            df = OrderModel.load_data()
            order = df[df['OrderID'] == int(order_id)]
            if order.empty:
                return jsonify({'error': 'Order not found'}), 404
            data = order.to_dict(orient='records')[0]
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def create_order(json_data):
        """Create a new order."""
        try:
            # Validate input data
            data = OrderModel.schema.load(json_data)
        except ValidationError as err:
            return jsonify({'errors': err.messages}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        try:
            df = OrderModel.load_data()
            if not df[df['OrderID'] == data['OrderID']].empty:
                return jsonify({'error': 'Order already exists'}), 400

            df = df.append(data, ignore_index=True)
            OrderModel.save_data(df)
            return jsonify(data), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    # @staticmethod
    # def update_order(order_id, json_data):
    #     """Update an existing order."""
    #     try:
    #         df = OrderModel.load_data()
    #         if df[df['OrderID'] == int(order_id)].empty:
    #             return jsonify({'error': 'Order not found'}), 404

    #         # Validate input data
    #         data = OrderModel.schema().load(json_data, partial=True)
    #     except ValidationError as err:
    #         return jsonify({'errors': err.messages}), 400
    #     except Exception as e:
    #         return jsonify({'error': str(e)}), 500

    #     try:
    #         df.loc[df['OrderID'] == int(order_id), data.keys()] = data.values()
    #         OrderModel.save_data(df)
    #         updated_order = df[df['OrderID'] == int(order_id)].to_dict(orient='records')[0]
    #         return jsonify(updated_order), 200
    #     except Exception as e:
    #         return jsonify({'error': str(e)}), 500
        
    @staticmethod    
    def update_order(order_id, data):
        df = pd.read_csv('Northwind_database_csv/orders.csv')
        if df[df['OrderID'] == order_id].empty:
            return jsonify({'error': 'Order not found'}), 404
        df.update(pd.DataFrame([data]))
        df.to_csv('Northwind_database_csv/orders.csv', index=False)
        return jsonify(data), 200
   

    @staticmethod
    def delete_order(order_id):
        """Delete an existing order."""
        try:
            df = OrderModel.load_data()
            if df[df['OrderID'] == int(order_id)].empty:
                return jsonify({'error': 'Order not found'}), 404

            df = df[df['OrderID'] != int(order_id)]
            OrderModel.save_data(df)
            return jsonify({'message': 'Order deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_orders_by_customer(customer_id):
        """Retrieve all orders for a specific customer."""
        try:
            df = OrderModel.load_data()
            orders = df[df['CustomerID'] == customer_id]
            if orders.empty:
                return jsonify({'error': 'No orders found for this customer'}), 404
            data = orders.to_dict(orient='records')
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# app/config.py
import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'Northwind_database_csv')
    CUSTOMERS_CSV = os.path.join(DATA_DIR, 'customers.csv')
    PRODUCTS_CSV = os.path.join(DATA_DIR, 'products.csv')
    ORDERS_CSV = os.path.join(DATA_DIR, 'orders.csv')

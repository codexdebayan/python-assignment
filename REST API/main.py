import os
import pandas as pd
from flask import Flask, json, request

# Define path
customer_file_path = 'Northwind_database_csv/customers.csv'

# Check if the path is correct
print(f"Checking file at: {customer_file_path}\n")

# List directory contents for debugging
if os.path.exists('Northwind_database_csv'):
    print("Directory contents:", os.listdir('Northwind_database_csv'))
else:
    print("Directory does not exist.")

# Check if file exists and read it
if os.path.exists(customer_file_path):
    df = pd.read_csv(customer_file_path)
    print(df.head())
else:
    print(f"File not found at {customer_file_path}")

from app.controllers.customer_controller import CustomerController

# Define the updated customer data as a dictionary
updated_customer_data = {
    "CustomerID": "PANUKI",
    "CompanyName": "Alfreds Futterkiste",
    "ContactName": "Maria Sanders",
    "ContactTitle": "Sales Executive",
    "Address": "Obere Str. 57",
    "City": "Berlin",
    "PostalCode": "12209",
    "Country": "Germany",
    "Phone": "030-0074321",
    "Fax": "030-0076545"
}

# Call the update_customer method directly with the customer ID and the updated data
response, status_code = CustomerController.update_customer("PANUKI", updated_customer_data)

# Print the response
print(f"Response: {response}")
print(f"Status Code: {status_code}")
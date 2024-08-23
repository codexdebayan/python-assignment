from app.controllers.customer_controller import CustomerController

# Define the new customer data as a dictionary
new_customer_data = {

    "Address": "Obere Str. 5",
    "City": "Berlin",
    "CompanyName": "Alfreds Futterkiste",
    "ContactName": "Maria Sanders",
    "ContactTitle": "Sales Executive",
    "Country": "Germany",
    "CustomerID": "NOWID",
    "Fax": "030-0076545",
    "Phone": "030-0074321",
    "PostalCode": "12209",
    "Region": "NaN"

}

# Call the add_customer method directly with the customer data
response = CustomerController.add_customer(new_customer_data)

# Print the response
print(response)

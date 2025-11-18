order_data = {
    "customer": {
        "first_name": "Bob",
        "last_name": "Johnson"
    },
    "items": [
        {"item_name": "Book",
         "price": 25.99
         },
        {"item_name": "Notebook",
         "price": 4.50
         },
        {"item_name": "Pen",
         "price": 1.20
         }
    ]
}

# 1. Customer's full name
full_name = f"{order_data['customer']['first_name']} {order_data['customer']['last_name']}"
print("Customer Full Name:", full_name)

# 2. Total price of all items
total_price = sum(item["price"] for item in order_data["items"])
print("Total Order Price:", total_price)

# 3. List of item names
item_names = [item["item_name"] for item in order_data["items"]]
print("Item Names:", item_names)
import pandas as pd
import random

# Product basic information (can be expanded as needed)
products = [
    {"product_id": "P001", "product_name": "Wireless Earbuds", "category": "Electronics"},
    {"product_id": "P002", "product_name": "Bluetooth Speaker", "category": "Electronics"},
    {"product_id": "P003", "product_name": "Smartwatch", "category": "Wearables"},
    {"product_id": "P004", "product_name": "Phone Case", "category": "Accessories"},
    {"product_id": "P005", "product_name": "Fitness Tracker", "category": "Wearables"},
    {"product_id": "P006", "product_name": "Laptop Stand", "category": "Office"},
]

# Generate random inventory data for each product
def generate_inventory(products):
    data = []
    for p in products:
        stock = random.randint(0, 50)
        threshold = random.randint(5, 20)
        data.append({
            "product_id": p["product_id"],
            "product_name": p["product_name"],
            "category": p["category"],
            "stock_quantity": stock,
            "restock_threshold": threshold
        })
    return pd.DataFrame(data)

# Generate and save as CSV
inventory_df = generate_inventory(products)
inventory_df.to_csv("inventory.csv", index=False)
print(inventory_df.head())

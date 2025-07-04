import pandas as pd
import random
from datetime import datetime, timedelta

# The same product list
products = [
    {"product_id": "P001", "product_name": "Wireless Earbuds"},
    {"product_id": "P002", "product_name": "Bluetooth Speaker"},
    {"product_id": "P003", "product_name": "Smartwatch"},
    {"product_id": "P004", "product_name": "Phone Case"},
    {"product_id": "P005", "product_name": "Fitness Tracker"},
    {"product_id": "P006", "product_name": "Laptop Stand"},
]


# Generate sales records
def generate_sales_data(num_sales=30, start_order_id=5001, start_date="2024-06-01"):
    data = []
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    for i in range(num_sales):
        order_id = start_order_id + i
        product = random.choice(products)
        quantity_sold = random.randint(1, 5)
        sale_date = base_date + timedelta(days=random.randint(0, 14))

        data.append({
            "order_id": order_id,
            "product_id": product["product_id"],
            "quantity_sold": quantity_sold,
            "sale_date": sale_date.strftime("%Y-%m-%d")
        })

    return pd.DataFrame(data)


sales_df = generate_sales_data(40)
sales_df.to_csv("sales.csv", index=False)
print(sales_df.head())

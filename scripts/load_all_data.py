import csv
from config import get_connection

def load_inventory(csv_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO inventory (product_id, product_name, category, stock_quantity, restock_threshold)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['product_id'], row['product_name'], row['category'], row['stock_quantity'], row['restock_threshold']))

    conn.commit()
    cursor.close()
    conn.close()


def load_sales(csv_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO sales (order_id, product_id, quantity_sold, sale_date)
                VALUES (%s, %s, %s, %s)
            """, (row['order_id'], row['product_id'], row['quantity_sold'], row['sale_date']))

    conn.commit()
    cursor.close()
    conn.close()


def load_reviews(csv_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO reviews (review_id, product_id, product_name, review_text, rating, review_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (row['review_id'], row['product_id'], row['product_name'], row['review_text'], row['rating'], row['review_date']))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    load_inventory("data/inventory.csv")
    load_sales("data/sales.csv")
    load_reviews("data/reviews.csv")

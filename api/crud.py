from scripts.config import get_connection

def fetch_all(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_inventory():
    return fetch_all("SELECT * FROM inventory")

def get_sales():
    return fetch_all("SELECT * FROM sales")

def get_reviews():
    return fetch_all("SELECT * FROM reviews")

from config import get_connection

def read_inventory():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # return rows as dicts

    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

if __name__ == "__main__":
    inventory = read_inventory()
    for item in inventory:
        print(item)

from config import get_connection
# this script is created to test out the db connection and run random queries
# this file reads the inventory table from the database

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

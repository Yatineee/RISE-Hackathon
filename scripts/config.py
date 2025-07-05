import mysql.connector

def get_connection():
    """Establish a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='product_analyzer'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
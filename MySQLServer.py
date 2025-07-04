import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',       
            password='your_mysql_password'    
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: Could not connect to MySQL server.\nDetails: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

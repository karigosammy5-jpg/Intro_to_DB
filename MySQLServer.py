import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # 1. Connect to the MySQL Server
        # IMPORTANT: Replace 'YOUR_PASSWORD' with the password you set during installation!
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sammy@20"
        )
        
        cursor = mydb.cursor()

        # 2. Try to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
            exit(1)

        # 3. Close the connection
        cursor.close()
        mydb.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    create_database()
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

connection = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER_NAME"),
    password = os.getenv("PASSWORD")
)

if connection:
    print("COnnected to DB server!")
else:
    print("Could not connect to BD server!")

cursor = connection.cursor()

query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

try:
    cursor.execute(query)

except mysql.connector.Error as e:
    print(e)

else:
    if cursor.warning_count < 1:
        print("Database successfully created!")
    else:
        print("The database already exists")

finally:
    cursor.close()
    connection.close()

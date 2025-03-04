import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="!1Abody123",
        database="lab3python"
    )


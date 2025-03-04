import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="!######", # write mySQL password  here
        database="lab3python"
    )


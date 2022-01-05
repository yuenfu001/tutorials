import mysql.connector as liu
from mysql.connector import Error

def createTable():
    connection = liu.connect(
        host = "localhost",
        user = "root",
        password = "Imranliu007",
        database = "ope"
    )
    print("connection to server and database successful")
    cur = connection.cursor()
    cur.execute("CREATE TABLE haa(firstname varchar(20), lastname varchar(20), gender varchar(10), color varchar(10));")
    connection.commit()
    print("table creation successful")
    cur.close()

table = createTable()
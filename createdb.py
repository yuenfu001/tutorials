import mysql.connector as opemipo
from mysql.connector import Error

def create_db(hostname, user_name, password):
    connection = None
    try:
        connection = opemipo.connect(
            host=hostname,
            user = user_name,
            passwd = password
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE ope")
        print("database creation successful")
    except Error as err:
        print(f"{err}")
        # print("{}".format(err)) crtl + /

db_create = create_db("localhost", "root", "Imranliu007")
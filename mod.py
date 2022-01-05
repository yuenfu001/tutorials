#estalbished connection python mySQL workbench
import mysql.connector as opemipo
from mysql.connector import Error

def server_conn(hostname, user_name, password):
    connection = None
    try:
        connection = opemipo.connect(
            host = hostname, 
            user = user_name, 
            passwd = password
            )
        cursor = connection.cursor()
        print("My server is connected")
    except Error as err:
        print(f"{err}")

server = server_conn("localhost", "root", "Imranliu007")

import mysql.connector as msql
import csv
import pandas as pd

def import_csv():
    conn = msql.connect(
        host = "localhost",
        user = "root",
        passwd = "Imranliu007",
        database = "ope"
    )
    data = str("C:\\Users\\XTUD10-xxxxxxxxxxxxx\\Desktop\\TASK 1a\\tutorials\\stuff.csv")
    # df = pd.read_csv(data, delimiter = ",")
    df = csv.reader(data, delimiter = ",")
    # df1 = pd.DataFrame(df)
    cursor = conn.cursor()
    # header = next(df)
    query = """ insert into ope.haa(firstname, lastname, gender,color) values(%s,%s,%s,%s) """
    for row in df:

        cursor.executemany(query,row)
    conn.commit()
    cursor.close()
    print("imported csv successful")

csv = import_csv()


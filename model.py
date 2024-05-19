import psycopg2
import connection as condb

def read_data_all(cur,table):
    query = f"SELECT * FROM {table}"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)

conn, cur = condb.connect()
read_data_all(cur,"tipe_kamar")
condb.close(conn, cur)

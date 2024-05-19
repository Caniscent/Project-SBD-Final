import psycopg2
import connection as condb

def read_data(cur,select = "*", table = "", orderby = ""):
    if orderby != "":
        query = f"SELECT {select} FROM {table} ORDER BY {orderby}"
    else:
        query = f"SELECT {select} FROM {table}"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)

conn, cur = condb.connect()
read_data(cur,select="id_tipe_kamar, harga",table="tipe_kamar",orderby="harga")
condb.close(conn, cur)

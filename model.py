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
    cur.close()
    conn.close()

    # Penulisan values menggunakan list. Ex: Values = ["data1",data2, "data3"]
def create_data(cur, table,values):
    column = column_data(cur, table)

    query_values = ""
    for i in values:
        if values == str():
            i = f"'{values}',"
        elif values == int() or values == float():
            i = f"{values},"
        else:
            continue
        query_values += i

    query = f"INSERT INTO {table}{tuple(column)}VALUES({query_values})"
    cur.execute(query,tuple(values))
    conn.commit()
    cur.close()
    conn.close()

def update_data():
    pass

def delete_data():
    pass

def column_data(cur, table):
    column_name = list()
    query_column= f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
    cur.execute(query_column)
    data2 = cur.fetchall()
    for i in data2:
        column_name.extend(i)
    return column_name


# Mains
conn, cur = condb.connect()
read_data(cur,table="tipe_kamar")

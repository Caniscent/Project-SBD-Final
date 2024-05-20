import psycopg2
import connection

def read_data(select = "*", table = "", orderby = ""):
    conn, cur = connection.connect()
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
    # Harus urut sesuai kolom di database
def create_data(table,values):
    conn, cur = connection.connect()
    column = column_data(table=table)

    query_values = []
    for i in values:
        if isinstance(i,str):
            result = f"'{i}'"
        elif isinstance(i,int) or isinstance(i,float):
            result = f"{i}"
        else:
            continue
        query_values.append(result)

    query = f"INSERT INTO {table}({",".join(column)})VALUES({",".join(query_values)})"
    # return query
    cur.execute(query,tuple(values))
    conn.commit()
    cur.close()
    conn.close()

def update_data():
    pass

def delete_data():
    pass

def column_data(table,idenable=0):
    conn, cur = connection.connect()
    column_name = []
    query_column= f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
    cur.execute(query_column)
    data = cur.fetchall()
    if idenable == 1:
        for i in data:
            column_name.extend(i)
    else:
        for i in data[1:]:
            column_name.extend(i)
    column_name = column_name[::-1]
    return column_name
    


# Menambah data
# print("Data Saat ini: ")
# read_data(table="fasilitas")
# new_nama_fasilitas = str(input("Nama Fasilitas: "))
# new_id_jenis_fasilitas = int(input("ID Fasilitas(1/2): "))
# values = [new_nama_fasilitas,new_id_jenis_fasilitas]
# create_data(table = "fasilitas", values= values)
# read_data(table="fasilitas")
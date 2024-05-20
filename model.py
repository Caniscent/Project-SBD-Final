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

    # Penulisan values menggunakan list. Ex: Values = ["data1",data2, "data3"]
def create_data(cur, table,values):
    column = column_data(cur=cur, table=table)

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

def update_data():
    pass

def delete_data():
    pass

def column_data(cur, table,idenable=0):
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
conn, cur = condb.connect()
print("Data Saat ini: ")
read_data(cur,table="fasilitas")
new_nama_fasilitas = str(input("Nama Fasilitas: "))
new_id_jenis_fasilitas = int(input("ID Fasilitas(1/2): "))
values = [new_nama_fasilitas,new_id_jenis_fasilitas]
create_data(cur,table = "fasilitas", values= values)
query_new_data = create_data(cur,table = "fasilitas", values= values)
read_data(cur,table="fasilitas")
cur.close()
conn.close()
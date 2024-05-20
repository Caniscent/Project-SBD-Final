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
    column = column_data(cur, table,idenable=0)

    query_values = list()
    for i in values:
        if values == str():
            i = f"'{values}'"
        elif values == int() or values == float():
            i = f"values"
        else:
            continue
        query_values.extend(i)

    query = f"INSERT INTO {table}({",".join(column)})VALUES({",".join(query_values)})"
    cur.execute(query,(values))
    conn.commit()
    print("Data berhasil ditambahkan!")

def update_data():
    pass

def delete_data():
    pass

def column_data(cur, table, idenable = 0):
    column_name = list()
    query_column= f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
    cur.execute(query_column)
    data2 = cur.fetchall()
    if idenable == 1:
        for i in data2[1:len(data2)]:
            column_name.extend(i)
    else:
        for i in data2:
            column_name.extend(i)
    return column_name
    


# Menambah data
conn, cur = condb.connect()
print("Data Saat ini: ")
read_data(cur,table="fasilitas")
new_nama_fasilitas = input("Nama Fasilitas: ")
new_id_jenis_fasilitas = int(input("ID Fasilitas(1/2): "))
values = [new_nama_fasilitas,new_id_jenis_fasilitas]
create_data(cur,table = "fasilitas", values= values)
read_data(cur,table="fasilitas")

# a = 2
# b = "Halo"
# text = f"{a}"
# print(text)
# print(type(text))

cur.close()
conn.close()
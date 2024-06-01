import psycopg2
import connection

def read_data(select = "*", table = "",columnid="" ,orderby = "",join_tables=None, join_conditions=None, where=None):
    conn, cur = connection.connect()
    column = column_data(table=table, idenable=True)
    Where = f"WHERE {where}"

    join_clause = ""
    if join_tables and join_conditions:
        for i in range(len(join_tables)):
            # join_table = join_tables[i]
            # join_condition = join_conditions[i]
            join_clause += f"JOIN {join_tables[i]} ON {join_conditions[i]} "

    if columnid !="":
        query = f"SELECT {select} FROM {table} {join_clause} WHERE {column[0]} = {columnid} "
        cur.execute(query)
        data = cur.fetchone()
        result = data
    else:
        if orderby != "":
            if join_tables and join_conditions:
                if where:
                    query = f"SELECT {select} FROM {table} {join_clause} {Where} ORDER BY {orderby}"
                else:
                    query = f"SELECT {select} FROM {table} {join_clause} ORDER BY {orderby}"
            else:
                query = f"SELECT {select} FROM {table} ORDER BY {orderby}"
        else:
            if where:
                query = f"SELECT {select} FROM {table} {join_clause} {Where}"
            else:
                query = f"SELECT {select} FROM {table} {join_clause}"
            # query = f"SELECT {select} FROM {table} {join_clause}"
        cur.execute(query)
        data = cur.fetchall()
        result = []
        for i in data:
            result.append(i)
    print(query)
    # exit()
    cur.close()
    conn.close()
    return result

    # Penulisan values menggunakan list. Ex: Values = ["data1",data2, "data3"]
    # Harus urut sesuai kolom di database
def create_data(table,values):
    conn, cur = connection.connect()
    column = column_data(table=table)

    query_values = []
    for i in values:
        if isinstance(i,str) and i != "":
            result = f"'{i}'"
        elif isinstance(i,int) or isinstance(i,float):
            result = f"{i}"
        elif i == None:
            result = f"NULL"
        else:
            continue
        query_values.append(result)

    query = f"""
    INSERT INTO {table} ({",".join(column)})
    VALUES ({",".join(query_values)})
    """
    # return query
    cur.execute(query,tuple(values))
    conn.commit()
    cur.close()
    conn.close()

def update_data(table,idcolomn,values):
    conn, cur = connection.connect()
    column = column_data(table=table,idenable=1)
    data = []
    i = 0

    for x in range(len(column)-1):
        query_values = []
        for y in values:
            if y == None or y == "None":
                result = f"NULL"
            else:
                if isinstance(y,str) and y != "":
                    result = f"'{y}'"
                elif isinstance(y,int) or isinstance(y,float):
                    result = f"{y}"
                else:
                    continue
            query_values.append(result)
        dump = f"{column[i+1]} = {query_values[i]}"
        data.append(dump)
        i += 1
    
    query = f"""
    UPDATE {table} SET {",".join(data)} 
    WHERE {column[0]} = {idcolomn}
    """
    cur.execute(query,tuple(values))
    conn.commit()
    cur.close()
    conn.close()

def delete_data(table,idcolumn,foreign_key="",foreign_table=""):
    conn, cur = connection.connect()
    column = column_data(table=table,idenable=1)

    primary_key_column = column[0]

    if foreign_key and foreign_table:
        foreign_query = f"DELETE FROM {foreign_table} WHERE {foreign_key} = {idcolumn}"
        cur.execute(foreign_query)

    query = f"DELETE FROM {table} WHERE {primary_key_column} = {idcolumn}"

    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def column_data(table,idenable=0):
    conn, cur = connection.connect()
    column_name = []
    query_column= f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position"
    cur.execute(query_column)
    data = cur.fetchall()
    if idenable == 1:
        for i in data:
            column_name.extend(i)
    else:
        for i in data[1:]:
            column_name.extend(i)
    return column_name
    


# Menambah data
# print("Data Saat ini: ")
# read_data(table="fasilitas")
# new_nama_fasilitas = str(input("Nama Fasilitas: "))
# new_id_jenis_fasilitas = int(input("ID Fasilitas(1/2): "))
# values = [new_nama_fasilitas,new_id_jenis_fasilitas]
# create_data(table = "fasilitas", values= values)
# read_data(table="fasilitas")

#Updata data
# table = "fasilitas"
# read = read_data(table=table)
# for i in read:
#     print(i)
# id_colomn = int(input("Masukkan ID Fasilitas: "))
# read = read_data(table=table,columnid=str(id_colomn))
# print("Data saat ini:")
# print(f"ID Fasilitas: {read[0]}")
# print(f"Nama Fasilitas: {read[1]}")
# print(f"Jenis Fasilitas: {read[2]}")
# print('-'*30)
# nama_fasilitas = input("Nama Fasilitas: ") or read[1]
# print("1. Umum\n2. Kamar")
# jenis_fasilitas = int(input("Jenis Fasilitas(1/2): ") or read[2])
# values = [nama_fasilitas,jenis_fasilitas]
# update_data(table=table,idcolomn=id_colomn,values=values)
# read = read_data(table=table)
# for i in read:
#     print(i)

# Delete Data
# table = "fasilitas"
# read = read_data(table=table)
# for i in read:
#     print(i)
# id_column = int(input(f"pilih ID {table} yang akan dihapus: "))
# read_column = read_data(table=table,columnid=id_column)
# print(f"ID Fasilitas: {read_column[0]}")
# print(f"Nama Fasilitas: {read_column[1]}")
# print(f"Jenis Fasilitas: {read_column[2]}")
# user = input("Yakin ingin menghapus?(Y/n) ")
# if user.lower() == 'y':
#     delete_data(table=table,idcolomn=id_column)
# else:
#     print("Data tidak jadi dihapus")

# read = read_data(table=table)
# for i in read:
#     print(i)
import connection
import model

# Tabel name identification
TabelFK = "fasilitas_kamar"
TabelKamar = "kamar"
TabelFasilitas = "fasilitas"
# Get column name
ColumnFK = model.column_data(table=TabelFK,idenable=True)
ColumnKamar = model.column_data(table=TabelKamar,idenable=True)
ColumnFasilitas = model.column_data(table=TabelFasilitas,idenable=True)

def CreateFK():
    try:
        print("Menambah Data Baru: ")
        DataKamar = model.read_data(table=TabelKamar)
        for i in DataKamar:
            print(i)
        Id_Kamar = input("Masukkan ID Kamar: ")
    except:
        pass
    finally:
        pass

def ReadFK():
    try:
        conn, cur = connection.connect()
        data = model.read_data(select=f"{TabelFK}.{ColumnFK[0]},{TabelKamar}.{ColumnKamar[1]},{TabelFasilitas}.{ColumnFasilitas[1]}",
                               table=TabelFK,
                               join_tables=[TabelKamar,TabelFasilitas],
                               join_conditions=[f"{TabelKamar}.{ColumnKamar[0]} = {TabelFK}.{ColumnFK[1]}",
                                                f"{TabelFasilitas}.{ColumnFasilitas[0]} = {TabelFK}.{ColumnFK[2]}"])
        for i in data:
            print(i)
    except Exception as e:
        print(f"Gagal membaca data! Error: {e}")
    finally:
        cur.close()
        conn.close()

def UpdateFK():
    try:
        pass
    except:
        pass
    finally:
        pass

def DeleteFK():
    try:
        pass
    except:
        pass
    finally:
        pass

def AksiFasilitasKamar():
    try:
        pass
    except:
        pass
    finally:
        pass

if __name__ == "__main__":
    pass
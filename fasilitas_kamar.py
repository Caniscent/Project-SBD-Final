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
        data = model.read_data(select=f"{TabelFK}.{ColumnFK[0]},{TabelKamar}.{ColumnKamar[1]},{TabelFasilitas}.{ColumnFasilitas[1]}",
                               table=TabelFK,
                               join_tables=[TabelKamar,TabelFasilitas],
                               join_conditions=[f"{TabelKamar}.{ColumnKamar[0]} = {TabelFK}.{ColumnFK[1]}",
                                                f"{TabelFasilitas}.{ColumnFasilitas[0]} = {TabelFK}.{ColumnFK[2]}"])
        for i in data:
            print(i)
    except Exception as e:
        print(f"Gagal membaca data! Error: {e}")

def UpdateFK():
    try:
        ReadFK()
        id_fk = input("Masukkan ID Fasilitas Kamar: ")
        dataFK = model.read_data(select=f"{TabelFK}.{ColumnFK[0]},{TabelKamar}.{ColumnKamar[1]},{TabelFasilitas}.{ColumnFasilitas[1]}",
                               table=TabelFK,
                               join_tables=[TabelKamar,TabelFasilitas],
                               join_conditions=[f"{TabelKamar}.{ColumnKamar[0]} = {TabelFK}.{ColumnFK[1]}",
                                                f"{TabelFasilitas}.{ColumnFasilitas[0]} = {TabelFK}.{ColumnFK[2]}"],
                                columnid=id_fk)
        print("Data saat ini: ")
        print(f"ID Fasilitas Kamar: {dataFK[0]}")
        print(f"Nonor Kamar: {dataFK[1]}")
        print(f"Fasilitas: {dataFK[2]}")
        print("\nUbah Data: ")
        data_kamar = model.read_data(table=TabelKamar)
        for i in data_kamar:
            print (i)
        nomor_kamar = input(f"Masukkan Nomor Kamar: ") or dataFK[1]
        nama_fasilitas = input(f"Masukkan Nama Fasilitas: ") or dataFK[2]
        values = [nomor_kamar,nama_fasilitas]
        model.update_data(table=TabelFK,idcolomn=id_fk,values=values)
    except Exception as ex:
        print(f"Error: {ex}")

def DeleteFK():
    try:
        ReadFK()
        req = input("Pilih ID yang ingin dihapus: ")
        model.delete_data(table=TabelFK,idcolumn=req)
    except Exception as ex:
        print(f"Error: {ex}")

def AksiFasilitasKamar():
    try:
        pass
    except:
        pass
    finally:
        pass

if __name__ == "__main__":
    pass
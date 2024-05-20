import model
import core
import connection
import main

tabel_fasilitas = "fasilitas"
tabel_jenis = "jenis_fasilitas"

def lihat_fasilitas(table_fasilitas):
    kolom = model.column_data(table=tabel_fasilitas, idenable=True)
    data = model.read_data(table=tabel_fasilitas)
    print(kolom)
    for i in data:
        print(i)

def tambah_fasilitas(table_fasilitas, table_jenis):
    new_nama_fasilitas = input("Nama Fasilitas : ")
    print(model.read_data(table=table_jenis))
    new_id_jenis_fasilitas = int(input("ID Jenis (1/2) : "))
    values = [new_nama_fasilitas, new_id_jenis_fasilitas]
    model.create_data(table_fasilitas, values)

def hapus_fasilitas(tabel_fasilitas):
    kolom = model.column_data(table=tabel_fasilitas, idenable=True)
    data = model.read_data(table=tabel_fasilitas)
    for i in data:
        print(i)
    pilih_id = int(input("Pilih ID data (Nomor) : "))
    model.delete_data(tabel_fasilitas, pilih_id)
    
def update_fasilitas(tabel_fasilitas, tabel_jenis):
    kolom = model.column_data(table=tabel_fasilitas, idenable=True)
    data = model.read_data(table=tabel_fasilitas)
    data_jenis = model.read_data(table=tabel_jenis)
    print(kolom)
    for i in data:
        print(i)
    pilih_id = int(input("Pilih Data (Nomor) : "))
    print("Data yang anda pilih : ")
    data = model.read_data(table=tabel_fasilitas, columnid=pilih_id)
    print("Nama Fasilitas : "+data[1])
    print("ID Jenis : "+ str(data[2]))
    print("== Masukkan Data Baru ==")
    new_nama_fasilitas = input("Masukkan Nama Fasilitas Baru (Enter untuk skip) : " or data[1])
    print(data_jenis)
    new_id_jenis_fasilitas = int(input("Masukkan ID Jenis (Enter untuk skip) : ") or data[2])
    values = [new_nama_fasilitas, new_id_jenis_fasilitas]
    model.update_data(tabel_fasilitas, pilih_id, values)

def aksi_fasilitas():
    core.clear()
    while True:
        print("[FASILITAS]")
        print("""Menu :
        1. Lihat Fasilitas
        2. Tambah Fasilitas
        3. Hapus Fasiltias
        4. Update Fasilitas
        5. Kembali
        """)

        input_user = input("Pilih Menu : ")

        match input_user:
            case "1":
                core.clear()
                lihat_fasilitas(tabel_fasilitas)
            case "2":
                tambah_fasilitas(tabel_fasilitas, tabel_jenis)
            case "3":
                core.clear()
                hapus_fasilitas(tabel_fasilitas)
            case "4":
                core.clear()
                update_fasilitas(tabel_fasilitas, tabel_jenis)
            case "5":
                core.clear()
                main.mainmenu()

import model
import core
import main
import connection

tabel_kamar="kamar"

def baca_kamar ():
    data = model.column_data(table=tabel_kamar,idenable=True)
    read = model.read_data(table=tabel_kamar)
    print(data)
    for i in read:
        print(i)

def tambah_kamar ():
    nama_kamar = input ("Masukkan Nomer Kamar: ")
    data_kamar = model.read_data(table="kamar")
    for i in data_kamar:
        print(i)
    print("ID 1 = Kamar Mandi Dalam\nID 2 = Kamar Mandi Luar")
    tipe_kamar_id = input ("masukkan ID Tipe Kamar: ")
    data_kamar = model.read_data(table="kamar")
    values = [nama_kamar,tipe_kamar_id]
    model.create_data(tabel_kamar,values)\
    
def ubah_kamar ():
    data = model.column_data(table=tabel_kamar,idenable=True)
    read = model.read_data(table=tabel_kamar)
    print(data)
    for i in read:
        print(i)
    pilih_id = int(input("Masukan ID Kamar : "))
    print("Data yang anda pilih : ")
    read = model.read_data(table=tabel_kamar, columnid=pilih_id)
    print(f"ID Kamar   : {read[0]}")
    print(f"Nomer Kamar: {read[1]}")
    print(f"Tipe Kamar : {read[2]}")
    print("== Masukkan Data Baru ==")
    nomor_kamar = input("Nomer Kamar Baru : ") or read[1]
    print("ID = 1 Kamar Mandi Dalam\nID 2 = Kamar Mandi Luar")
    tipe_kamar = int(input("ID Tipe Kamar Baru (1/2): ") or read[2])
    values = [nomor_kamar,tipe_kamar]
    model.update_data(tabel_kamar, pilih_id,values)

def hapus_kamar():
    data = model.column_data(table=tabel_kamar,idenable=True)
    read = model.read_data(table=tabel_kamar)
    for i in read:
        print(i)
    pilih_id = int(input("Pilih ID data (Nomor) : "))
    user = input("Yakin ingin menghapus?(Y/n) ")
    if user.lower() == 'y':
        model.delete_data(table=tabel_kamar,idcolumn=pilih_id)
    else:
        print("Data tidak jadi dihapus")
# def tambah_kamar()
def aksi_kamar():
    core.clear()
    while True:
        print(" [KAMAR]")
        print("""| Menu:
    1. Menambah data kamar
    2. Data kamar
    3. Edit data kamar
    4. Hapus data kamar 
    5. Kembali
    """)   
        input_usr = input("|> Pilih Menu: ")
        
        match input_usr :
            case "1":
                core.clear
                tambah_kamar()
            case "2": 
                core.clear
                baca_kamar()
            case "3":
                core.clear()
                ubah_kamar()
            case "4":
                core.clear()
                hapus_kamar()
            case "5":
                core.clear()
                main.mainmenu()





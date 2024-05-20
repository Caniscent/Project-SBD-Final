import model
import core

table = "penghuni"

def new_penghuni():
    nik_penghuni = input("| Masukkan NIK\t: ")
    nama_penghuni = input("| Masukkan Nama Lengkap\t: ")
    no_telepon_penghuni = input("| Nomor Telepon\t: ")
    print("Format Tanggal Masuk = yyyy-mm-dd hh:mm:ss")
    tanggal_masuk = input("| Tanggal Masuk\t: ")
    tanggal_keluar = None
    data_kamar = model.read_data(table="kamar")
    for i in data_kamar:
        print(i)
    kamar_id = input("| Kamar\t: ")

    values = [nik_penghuni,nama_penghuni,no_telepon_penghuni,tanggal_masuk,tanggal_keluar,kamar_id]
    
    model.create_data(table=table,values=values)

def data_penghuni():
    column = model.column_data(table=table, idenable=True)
    read = model.read_data(table=table)
    print(column)
    for i in read:
        print(i)
    req = input("")

def edit_penghuni():
    pass

def hapus_penghuni():
    pass


if __name__ == "__main__":
    while True:
        core.clear()
        print(" [PENGHUNI]")
        print("""| Menu:
    1. Menambah data penghuni
    2. Data penghuni
    3. Edit data penghuni
    4. Hapus dana penghuni 
    """)   
        input_usr = input("|> Pilih Menu: ")
        if input_usr == '1':
            core.clear()
            new_penghuni()
        elif input_usr == '2':
            data_penghuni()
        elif input_usr == '3':
            edit_penghuni()
        elif input_usr == '4':
            hapus_penghuni()
        else:
            req = input("")
            core.clear()

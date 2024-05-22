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
    kolom = model.column_data(table=table, idenable=True)
    data = model.read_data(table=table)
    data_kamar = model.read_data(table="kamar")
    print(kolom)
    for i in data:
        print(i)
    pilih_id = int(input("Pilih Data (Nomor) : "))
    print("Data yang anda pilih : ")
    data = model.read_data(table=table, columnid=pilih_id)
    print("NIK Penghuni : "+ data[1])
    print("Nama Penghuni: "+ data[2])
    print("Nomor Telepon: "+ data[3])
    print("Tanggal Masuk: "+ str(data[4]))
    print("Tanggal Keluar: "+ str(data[5]))
    data_kamar_penghuni = model.read_data(table="kamar",columnid=pilih_id)
    print("Nomor Kamar: "+ data_kamar_penghuni[1])
    print("== Masukkan Data Baru ==")
    nik_penghuni = input("Masukkan NIK (Enter untuk skip) : ") or data[1]
    nama_penghuni = input("Masukkan Nama Lengkap (Enter untuk skip) : ") or data[2]
    no_telepon_penghuni = input("Masukkan No telepon penghuni: ") or data[3]
    tanggal_masuk = input("Masukkan tanggal masuk dengan format YYYY-MM-DD HH:MM:SS: ") or str(data[4])
    tanggal_keluar = input("Masukkan tanggal keluar dengan format YYYY-MM-DD HH:MM:SS (Opsional): ") or str(data[5])
    for i in data_kamar:
        print(i)
    kamar_id = input("Masukkan ID Kamar: ") or data[6]

    values = [nik_penghuni,nama_penghuni,no_telepon_penghuni,tanggal_masuk,tanggal_keluar,kamar_id]
    model.update_data(table, pilih_id, values)

def hapus_penghuni():
    pass

def aksi_penghuni():
    while True:
        core.clear()
        print(" [PENGHUNI]")
        print("""| Menu:
    1. Menambah data penghuni
    2. Lihat Data penghuni
    3. Perbarui data penghuni
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


if __name__ == "__main__":
    aksi_penghuni()
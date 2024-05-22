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
    # column = model.column_data(table=table, idenable=True)
    read = model.read_data(table=table,orderby="id_penghuni")
    # print(column)
    # for i in read:
    #     print(i)
    if read:
        print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar ID':<5}")
        print("-" * 140)
        for row in read:
            id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk, tanggal_keluar, kamar_id = row
            print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
    else:
        print("Tidak ada data kondisi fasilitas yang tersedia.")
    req = input("")

def edit_penghuni():
    # kolom = model.column_data(table=table, idenable=True)
    data = model.read_data(table=table,orderby="id_penghuni")
    data_kamar = model.read_data(table="kamar")
    # print(kolom)
    if data:
        print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar ID':<5}")
        print("-" * 140)
        for row in data:
            id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk, tanggal_keluar, kamar_id = row
            print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
    else:
        print("Tidak ada data kondisi fasilitas yang tersedia.")
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
    read = model.read_data(table=table,orderby="id_penghuni")
    if read:
        print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar ID':<5}")
        print("-" * 140)
        for row in read:
            id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk, tanggal_keluar, kamar_id = row
            print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
    else:
        print("Tidak ada data kondisi fasilitas yang tersedia.")
    id_column = int(input(f"pilih ID {table} yang akan dihapus: "))
    read_column = model.read_data(table=table,columnid=id_column)
    print(f"ID Penghuni: {read_column[0]}")
    print(f"NIK Penghuni: {read_column[1]}")
    print(f"Nama Penghuni: {read_column[2]}")
    user = input("Yakin ingin menghapus?(Y/n) ")
    if user.lower() == 'y':
        model.delete_data(table=table,idcolomn=id_column)
    else:
        print("Data tidak jadi dihapus")

    read = model.read_data(table=table)
    for i in read:
        print(i)

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
import model
import core

table = "penghuni"

def new_penghuni():
    while True:
        nik_penghuni = input("| Masukkan NIK\t: ")
        nama_penghuni = input("| Masukkan Nama Lengkap\t: ")
        no_telepon_penghuni = input("| Nomor Telepon\t: ")
        print("Format Tanggal Masuk = yyyy-mm-dd hh:mm:ss")
        tanggal_masuk = input("| Tanggal Masuk\t: ")
        tanggal_keluar = input("| Tanggal Keluar(opsional\t: ")
        data_kamar = model.read_data(table="kamar")
        for i in data_kamar:
            print(i)
        kamar_id = input("| Kamar\t: ")

        if not (nik_penghuni and nama_penghuni and no_telepon_penghuni and tanggal_masuk and kamar_id):
            print('\n[ DATA TIDAK LENGKAP ]')
            print('Klik ENTER untuk melanjutkan!')
            enter = input()
            core.clear()
            break

        data = model.read_data(table=table)
        data_ada = [cek[1] for cek in data]
        # for cek in data[1:]:
        #     data_ada.append(cek[1])
        if nik_penghuni in data_ada:
            print('\n[ PENGHUNI DENGAN NIK INI SUDAH ADA ]')
            print('Klik ENTER untuk melanjutkan!')
            enter = input()
            core.clear()
            break


        if tanggal_keluar:
            values = [nik_penghuni,nama_penghuni,no_telepon_penghuni,tanggal_masuk,tanggal_keluar,kamar_id]
        else:
            values = [nik_penghuni,nama_penghuni,no_telepon_penghuni,tanggal_masuk,None,kamar_id]

        model.create_data(table=table,values=values)
        print("\n[Data penghuni sudah ditambahkan]")
        req = input('Klik ENTER untuk melanjutkan!')
        core.clear()
        break
    

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
        print("[Tidak ada data penghuni yang tersedia]")
    req = input("")

def edit_penghuni():
    while True:
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
            print("[Tidak ada data penghuni yang tersedia]")
        pilih_id = input("Pilih Data (Nomor) : ")
        if pilih_id:
            try:    
                pilih_id = int(pilih_id)
                if any(id_penghuni == pilih_id for id_penghuni, _, _, _, _, _, _ in data):
                    print("Data yang anda pilih : ")
                    data_column = model.read_data(table=table, columnid=pilih_id)
                    print("NIK Penghuni : "+ data_column[1])
                    print("Nama Penghuni: "+ data_column[2])
                    print("Nomor Telepon: "+ data_column[3])
                    print("Tanggal Masuk: "+ str(data_column[4]))
                    print("Tanggal Keluar: "+ str(data_column[5]))
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

                    if tanggal_keluar:
                        values = [nik_penghuni,nama_penghuni,no_telepon_penghuni,tanggal_masuk,tanggal_keluar,kamar_id]
                    else:
                        values = [nik_penghuni,nama_penghuni,no_telepon_penghuni,tanggal_masuk,None,kamar_id]

                    model.update_data(table, pilih_id, values)
                    print("\n[Data penghuni sudah diperbarui]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    break
                    
                else:
                    print("\n[Data tidak ada!]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    continue
            except ValueError:
                print("\n[Id harus berupa angka saja!]")
                req = input('Klik ENTER untuk melanjutkan!')
                core.clear()
                continue

        else:
            core.clear()
            continue
        

def hapus_penghuni():
    while True:
        read = model.read_data(table=table,orderby="id_penghuni")
        if read:
            print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar ID':<5}")
            print("-" * 140)
            for row in read:
                id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk, tanggal_keluar, kamar_id = row
                print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
        else:
            print("[Tidak ada data penghuni yang tersedia]")
        id_column = input(f"pilih ID {table} yang akan dihapus: ")
        if id_column:
            try:    
                id_column = int(id_column)
                if any(id_penghuni == id_column for id_penghuni, _, _, _, _, _, _ in read):
                    read_column = model.read_data(table=table,columnid=id_column)
                    print(f"ID Penghuni: {read_column[0]}")
                    print(f"NIK Penghuni: {read_column[1]}")
                    print(f"Nama Penghuni: {read_column[2]}")
                    user = input("Yakin ingin menghapus?(Y/n) ")
                    if user.lower() == 'y':
                        model.delete_data(table=table,idcolumn=id_column)
                        print('\n[Data penghuni sudah dihapus]')
                        req = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        break
                    else:
                        print("\n[Data penghuni tidak jadi dihapus]")
                        req = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        break
                    
                else:
                    print("\n[Data tidak ada!]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    continue
            except ValueError:
                print("\n[Id harus berupa angka saja!]")
                req = input('Klik ENTER untuk melanjutkan!')
                core.clear()
                continue

        else:
            core.clear()
            continue
        

        # read = model.read_data(table=table)
        # for i in read:
        #     print(i)

def aksi_penghuni():
    while True:
        core.clear()
        print(" [PENGHUNI]")
        print("""
| Menu:
1. Lihat Data penghuni
2. Menambah data penghuni
3. Perbarui data penghuni
4. Hapus dana penghuni 
9. Kembali
    """)   
        input_usr = input("|> Pilih Menu: ")
        if input_usr == '1':
            data_penghuni()
            core.clear()
        elif input_usr == '2':
            new_penghuni()
            core.clear()
        elif input_usr == '3':
            edit_penghuni()
            core.clear()
        elif input_usr == '4':
            hapus_penghuni()
            core.clear()
        elif input_usr == '9':
            core.clear()
            break
        else:
            req = input("")
            core.clear()


if __name__ == "__main__":
    aksi_penghuni()
import model
import core
import main
import connection

tabel_kamar="kamar"
tabel_penghuni="penghuni"

def baca_kamar ():
    data = model.read_data(select="k.id_kamar, k.nomor_kamar, tk.nama_tipe_kamar",
                           table="kamar k",
                           orderby="id_kamar",
                           join_tables=["tipe_kamar tk"],
                           join_conditions=["k.tipe_kamar_id = tk.id_tipe_kamar"])
    
    if data:
        print(f"{'ID':<5} {'Nomor Kamar':<12} {'Tipe Kamar':<10}")
        print("-" * 36)
        for row in data:
            id_kamar, nomor_kamar, tipe_kamar_id = row
            print(f"{id_kamar:<5} {nomor_kamar:<12} {tipe_kamar_id:<10}")
    else:
        print("[Tidak ada data kamar yang tersedia]")

    req = input("Klik ENTER untuk kembali...")

def tambah_kamar ():
    while True:
        nomor_kamar = input ("Masukkan Nomor Kamar: ")
        data_kamar = model.read_data(table="kamar")
        for i in data_kamar:
            print(i)
        print("ID 1 = Kamar Mandi Dalam\nID 2 = Kamar Mandi Luar")
        tipe_kamar_id = input ("masukkan ID Tipe Kamar: ")
        if not (nomor_kamar and tipe_kamar_id):
            print('\n[ DATA TIDAK LENGKAP ]')
            print('Klik ENTER untuk melanjutkan!')
            enter = input()
            core.clear()
            break

        data = model.read_data(table="kamar")
        data_ada = [cek[1] for cek in data]
        # for cek in data[1:]:
        #     data_ada.append(cek[1])
        if nomor_kamar in data_ada:
            print('\n[ KAMAR DENGAN NOMOR INI SUDAH ADA ]')
            print('Klik ENTER untuk melanjutkan!')
            enter = input()
            core.clear()
            break

        values = [nomor_kamar,tipe_kamar_id]
        model.create_data(tabel_kamar,values)
        print("\n[Data kamar sudah ditambahkan]")
        req = input('Klik ENTER untuk melanjutkan!')
        core.clear()
        break

def ubah_kamar ():
    while True:
        # data = model.column_data(table=tabel_kamar,idenable=True)
        # read = read_join()
        # print(data)
        read = model.read_data(select="k.id_kamar, k.nomor_kamar, tk.nama_tipe_kamar",
                           table="kamar k",
                           orderby="id_kamar",
                           join_tables=["tipe_kamar tk"],
                           join_conditions=["k.tipe_kamar_id = tk.id_tipe_kamar"])
        if read:
            print(f"{'ID':<5} {'Nomor Kamar':<12} {'Tipe Kamar':<10}")
            print("-" * 36)
            for row in read:
                id_kamar, nomor_kamar, tipe_kamar_id = row
                print(f"{id_kamar:<5} {nomor_kamar:<12} {tipe_kamar_id:<10}")
        else:
            print("[Tidak ada data kamar yang tersedia]")
            req = input('Klik ENTER untuk melanjutkan!')
            core.clear()
            break

        pilih_id = input("Masukan ID Kamar : ")
        if pilih_id:
            try:    
                pilih_id = int(pilih_id)
                if any(id_kamar == pilih_id for id_kamar, _, _ in read):
                    print("Data yang anda pilih : ")
                    read_column = model.read_data(table=tabel_kamar, columnid=pilih_id)
                    print(f"ID Kamar   : {read_column[0]}")
                    print(f"Nomer Kamar: {read_column[1]}")
                    print(f"Tipe Kamar : {read_column[2]}")
                    print("== Masukkan Data Baru ==")
                    nomor_kamar = input("Nomer Kamar Baru : ") or read[1]
                    print("ID = 1 Kamar Mandi Dalam\nID 2 = Kamar Mandi Luar")
                    tipe_kamar = int(input("ID Tipe Kamar Baru (1/2): ") or read[2])
                    values = [nomor_kamar,tipe_kamar]
                    model.update_data(tabel_kamar, pilih_id,values)
                    print("\n[Data kamar sudah diperbarui]")
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
        

def hapus_kamar():
    while True:
        # data = model.column_data(table=tabel_kamar,idenable=True)
        # read = read_join()
        read = model.read_data(select="k.id_kamar, k.nomor_kamar, tk.nama_tipe_kamar",
                           table="kamar k",
                           orderby="id_kamar",
                           join_tables=["tipe_kamar tk"],
                           join_conditions=["k.tipe_kamar_id = tk.id_tipe_kamar"])
        if read:
            print(f"{'ID':<5} {'Nomor Kamar':<12} {'Tipe Kamar':<10}")
            print("-" * 36)
            for row in read:
                id_kamar, nomor_kamar, tipe_kamar = row
                print(f"{id_kamar:<5} {nomor_kamar:<12} {tipe_kamar:<10}")
        else:
            print("[Tidak ada data kamar yang tersedia]")
            req = input('Klik ENTER untuk melanjutkan!')
            core.clear()
            break

        pilih_id = input("Pilih ID data (Nomor): ")
        if pilih_id:
            try:    
                pilih_id = int(pilih_id)
                if any(id_kamar == pilih_id for id_kamar, _, _ in read):
                    user = input("Yakin ingin menghapus?(Y/n) ")
                    if user.lower() == 'y':
                        model.delete_data(table=tabel_kamar,idcolumn=pilih_id,foreign_key="kamar_id",foreign_table=tabel_penghuni)
                        print('\n[Data kamar sudah dihapus]')
                        if "kamar_id" == True:
                            print(f'[Menghapus data yang menggunakan foreign key dari tabel {tabel_penghuni}]')
                        req = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        break
                    else:
                        print("\n[Data kamar tidak jadi dihapus]")
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

        
# def tambah_kamar()
def aksi_kamar():
    core.clear()
    while True:
        print(" [ KAMAR ]")
        print("""
| Menu:
1. Lihat data kamar
2. Menambah data kamar
3. Perbarui data kamar
4. Hapus data kamar 
9. Kembali
""")   
        input_usr = input("|> Pilih Menu: ")
        
        match input_usr :
            case "1": 
                core.clear
                baca_kamar()
            case "2":
                core.clear
                tambah_kamar()
            case "3":
                core.clear()
                ubah_kamar()
            case "4":
                core.clear()
                hapus_kamar()
            case "9":
                core.clear()
                main.mainmenu()



if __name__ == "__main__":
    aksi_kamar()
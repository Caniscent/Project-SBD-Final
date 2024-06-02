import model
import connection
import datetime
import core
import main
from dateutil.relativedelta import relativedelta

table = "penghuni"

def new_penghuni():
    while True:
        nik_penghuni = input("| Masukkan NIK\t: ")
        nama_penghuni = input("| Masukkan Nama Lengkap\t: ")
        no_telepon_penghuni = input("| Nomor Telepon\t: ")
        print("Format Tanggal = yyyy-mm-dd hh:mm:ss")
        tanggal_masuk = input("| Tanggal Masuk (enter for now)\t: ") or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tanggal_keluar = input("| Tanggal Keluar(opsional)\t: ")
        data_kamar = model.read_data(select="k.*, tk.nama_tipe_kamar",
                                     table="kamar k",
                                     join_tables=["penghuni p", "tipe_kamar tk"],
                                     join_conditions=["p.kamar_id = k.id_kamar", "k.tipe_kamar_id = tk.id_tipe_kamar"],
                                     where="p.kamar_id IS NULL",
                                     join_type="LEFT"
                                     )
        if data_kamar:
            print(f"{'ID':<5} {'Nomor Kamar':<12} {'Tipe Kamar':<17}")
            print("-" * 43)
            for row in data_kamar:
                id_kamar, nomor_kamar = row[0:2]
                tipe_kamar_id = row[3]
                print(f"{id_kamar:<5} {nomor_kamar:<12} {tipe_kamar_id:<17}")
        else:
            print("[Tidak ada data kamar yang tersedia]")
        kamar_id = input("| Kamar\t: ")
        
        if not (nik_penghuni and nama_penghuni and no_telepon_penghuni and tanggal_masuk and kamar_id):
            print('\n[ DATA TIDAK LENGKAP ]')
            print('Klik ENTER untuk melanjutkan!')
            enter = input()
            core.clear()
            break

        data = model.read_data(table=table)
        data_ada = [cek[1] for cek in data]
        
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
    read = model.read_data(select="p.*, k.nomor_kamar",
                           table="penghuni p",
                           join_tables=["kamar k"],
                           join_conditions=["p.kamar_id = k.id_kamar"],
                           orderby="id_penghuni")
    if read:
        print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar':<5}")
        print("-" * 140)
        for row in read:
            id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk = row[0:5] 
            tanggal_keluar = "Masih Aktif" if row[5]==None else row[5]
            kamar_id = row[7]
            print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
        req = input('Klik ENTER untuk melanjutkan!')
        core.clear()
    else:
        print("[Tidak ada data penghuni yang tersedia]")
    req = input("")

def edit_penghuni():
    while True:
        data = model.read_data(select="p.*, k.nomor_kamar",
                           table="penghuni p",
                           join_tables=["kamar k"],
                           join_conditions=["p.kamar_id = k.id_kamar"],
                           orderby="id_penghuni")
        if data:
            print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar':<5}")
            print("-" * 140)
            for row in data:
                id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk = row[0:5] 
                tanggal_keluar = "Masih Aktif" if row[5]==None else row[5]
                kamar_id = row[7]
                print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
        else:
            print("[Tidak ada data penghuni yang tersedia]")
        pilih_id = input("Pilih Data (ID) : ")
        if pilih_id:
            try:    
                pilih_id = int(pilih_id)
                if any(id_penghuni == pilih_id for id_penghuni, _, _, _, _, _, _, _ in data):
                    print("Data yang anda pilih : ")
                    data_kamar_penghuni = model.read_data(select="penghuni.*, k.nomor_kamar",
                           table="penghuni",
                           join_tables=["kamar k"],
                           join_conditions=["penghuni.kamar_id = k.id_kamar"],columnid=pilih_id)
                    print("NIK Penghuni : "+ data_kamar_penghuni[1])
                    print("Nama Penghuni: "+ data_kamar_penghuni[2])
                    print("Nomor Telepon: "+ data_kamar_penghuni[3])
                    print("Tanggal Masuk: "+ str(data_kamar_penghuni[4]))
                    print("Tanggal Keluar: "+ str(data_kamar_penghuni[5]))
                    print("Nomor Kamar: "+ data_kamar_penghuni[7])
                    print("== Masukkan Data Baru ==")
                    nik_penghuni = input("Masukkan NIK (Enter untuk skip) : ") or data_kamar_penghuni[1]
                    nama_penghuni = input("Masukkan Nama Lengkap (Enter untuk skip) : ") or data_kamar_penghuni[2]
                    no_telepon_penghuni = input("Masukkan No telepon penghuni: ") or data_kamar_penghuni[3]
                    tanggal_masuk = input("Masukkan tanggal masuk dengan format YYYY-MM-DD HH:MM:SS: ") or str(data_kamar_penghuni[4])
                    tanggal_keluar = input("Masukkan tanggal keluar dengan format YYYY-MM-DD HH:MM:SS (Opsional): ") or str(data_kamar_penghuni[5])
                    data_kamar = model.read_data(select="k.*, tk.nama_tipe_kamar",
                                     table="kamar k",
                                     join_tables=["penghuni p", "tipe_kamar tk"],
                                     join_conditions=["p.kamar_id = k.id_kamar", "k.tipe_kamar_id = tk.id_tipe_kamar"],
                                     where="p.kamar_id IS NULL",
                                     join_type="LEFT"
                                     )
                    if data_kamar:
                        print(f"{'ID':<5} {'Nomor Kamar':<12} {'Tipe Kamar':<17}")
                        print("-" * 43)
                        for row in data_kamar:
                            id_kamar, nomor_kamar = row[0:2]
                            tipe_kamar_id = row[3]
                            print(f"{id_kamar:<5} {nomor_kamar:<12} {tipe_kamar_id:<17}")
                    else:
                        print("[Tidak ada data kamar yang tersedia]")
                    # for i in data_kamar:
                    #     print(i)
                    kamar_id = input("Masukkan ID Kamar: ") or data_kamar_penghuni[6]

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
            break
        

def hapus_penghuni():
    while True:
        read = model.read_data(select="p.*, k.nomor_kamar",
                           table="penghuni p",
                           join_tables=["kamar k"],
                           join_conditions=["p.kamar_id = k.id_kamar"],
                           orderby="id_penghuni")
        if read:
            print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar':<5}")
            print("-" * 140)
            for row in read:
                id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk = row[0:5] 
                tanggal_keluar = "Masih Aktif" if row[5]==None else row[5]
                kamar_id = row[7]
                print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
        else:
            print("[Tidak ada data penghuni yang tersedia]")
        id_column = input(f"pilih ID Penghuni yang akan dihapus: ")
    
        if id_column:
            try:    
                id_column = int(id_column)
                if any(id_penghuni == id_column for id_penghuni, _, _, _, _, _, _, _ in read):
                    data_kamar_penghuni = model.read_data(select="penghuni.*, k.nomor_kamar",
                           table="penghuni",
                           join_tables=["kamar k"],
                           join_conditions=["penghuni.kamar_id = k.id_kamar"],
                           columnid=int(id_column))
                    print(f"ID Penghuni: {data_kamar_penghuni[0]}")
                    print(f"NIK Penghuni: {data_kamar_penghuni[1]}")
                    print(f"Nama Penghuni: {data_kamar_penghuni[2]}")
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
            break
        
def aksi_penghuni():
    while True:
        core.clear()
        print(" [PENGHUNI]")
        print("""
| Menu:
1. Lihat Data penghuni
2. Menambah data penghuni
3. Perbarui data penghuni
4. Hapus data penghuni 
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
import model
import core
import connection
import main

tabel_fasilitas = "fasilitas"
tabel_jenis = "jenis_fasilitas"
tabel_status_fasilitas = "status_fasilitas"
# join_table = ["jenis_fasilitas jf"]
# join_condition = ["jf.id_jenis_fasilitas = f.jenis_fasilitas_id"]

def lihat_fasilitas():
    # kolom = model.column_data(table=tabel_fasilitas, idenable=True)
    data = model.read_data(select="f.id_fasilitas, f.nama_fasilitas, jf.nama_jenis_fasilitas",
                           table="fasilitas f",
                           orderby="id_fasilitas",
                           join_tables=["jenis_fasilitas jf"], 
                           join_conditions=["jf.id_jenis_fasilitas = f.jenis_fasilitas_id"]
    )
    # print(kolom)
    if data:
        print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Jenis Fasilitas':<5}")
        print("-" * 42)
        for row in data:
            id_users, nama_fasilitas, jenis_fasilitas = row
            print(f"{id_users:<5} {nama_fasilitas:<20} {jenis_fasilitas:<5}")
    else:
        print("[Tidak ada data fasilitas yang tersedia]")

def tambah_fasilitas(table_fasilitas, table_jenis):
    new_nama_fasilitas = input("Nama Fasilitas : ")
    print(model.read_data(table=table_jenis))
    new_id_jenis_fasilitas = int(input("ID Jenis (1/2) : "))

    if not (new_nama_fasilitas and new_id_jenis_fasilitas):
        print('\n[ DATA TIDAK LENGKAP ]')
        print('Klik ENTER untuk melanjutkan!')
        enter = input()
        core.clear()
    data = model.read_data(table="users")  
    data_ada = []
    for cek in data[1:]:
        data_ada.append(cek[1])
        if new_nama_fasilitas in data_ada:
            print('\n[ FASILITAS INI SUDAH ADA ]')
            print('Klik ENTER untuk melanjutkan!')
            enter = input()
            core.clear()

    values = [new_nama_fasilitas, new_id_jenis_fasilitas]
    model.create_data(table_fasilitas, values)
    print("\n[Data sudah ditambahkan]")
    req = input('Klik ENTER untuk melanjutkan!')
    core.clear()


def hapus_fasilitas(tabel_fasilitas,tabel_status_fasilitas):
    while True:
        # kolom = model.column_data(table=tabel_fasilitas, idenable=True)
        data = model.read_data(select="f.id_fasilitas, f.nama_fasilitas, jf.nama_jenis_fasilitas",
                               table="fasilitas f",
                               orderby="id_fasilitas",
                               join_tables=["jenis_fasilitas jf"], 
                               join_conditions=["jf.id_jenis_fasilitas = f.jenis_fasilitas_id"],
                               )
        if data:
            print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Jenis Fasilitas':<5}")
            print("-" * 42)
            for row in data:
                id_fasilitas, nama_fasilitas, jenis_fasilitas = row
                print(f"{id_fasilitas:<5} {nama_fasilitas:<20} {jenis_fasilitas:<5}")
        else:
            print("[Tidak ada data user yang tersedia]")

        pilih_id = input("Pilih ID data (Nomor) : ")
        if pilih_id:
            try:    
                pilih_id = int(pilih_id)
                if any(id_fasilitas == pilih_id for id_fasilitas, _, _ in data):
                    data_column = model.read_data(select="fasilitas.id_fasilitas, fasilitas.nama_fasilitas, jf.nama_jenis_fasilitas",
                                              table="fasilitas",
                                              orderby="id_fasilitas",
                                              join_tables=["jenis_fasilitas jf"], 
                                              join_conditions=["jf.id_jenis_fasilitas = fasilitas.jenis_fasilitas_id"],
                                              columnid=pilih_id)
                    print(f"""
ID Fasilitas: {data_column[0]}
Nama Fasilitas: {data_column[1]}
Jenis Fasilitas: {data_column[2]}
""")
                    user = input('Yakin ingin menghapus fasilitas(Y/n)? ')
                    if user.lower() == 'y':
                        model.delete_data(tabel_fasilitas, pilih_id, foreign_key="fasilitas_id", foreign_table=tabel_status_fasilitas)
                        print("\n[Data sudah dihapus]")
                        req = input('Klik ENTER untuk melanjutkan!')
                        break
                    else:
                        print("\n[Data tidak jadi dihapus]")
                        req = input('Klik ENTER untuk melanjutkan!')
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
    
def update_fasilitas(tabel_fasilitas, tabel_jenis):
    data = model.read_data(select="f.id_fasilitas, f.nama_fasilitas, jf.nama_jenis_fasilitas",
                        table="fasilitas f",
                        orderby="id_fasilitas",
                        join_tables=["jenis_fasilitas jf"], 
                        join_conditions=["jf.id_jenis_fasilitas = f.jenis_fasilitas_id"])
    
    data_jenis = model.read_data(table=tabel_jenis)

    if data:
        print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Jenis Fasilitas':<5}")
        print("-" * 42)
        for row in data:
            id_fasilitas, nama_fasilitas, jenis_fasilitas = row
            print(f"{id_fasilitas:<5} {nama_fasilitas:<20} {jenis_fasilitas:<5}")
    else:
        print("[Tidak ada data user yang tersedia]")
    
    pilih_id = input("Pilih ID  : ")
    if pilih_id:
        try:    
            pilih_id = int(pilih_id)
            if any(id_fasilitas == pilih_id for id_fasilitas, _, _ in data):
                print("Data yang anda pilih : ")
                data_column = model.read_data(select="fasilitas.nama_fasilitas, jf.nama_jenis_fasilitas",
                                              table="fasilitas",
                                              orderby="id_fasilitas",
                                              join_tables=["jenis_fasilitas jf"], 
                                              join_conditions=["jf.id_jenis_fasilitas = fasilitas.jenis_fasilitas_id"],
                                              columnid=pilih_id)
                # print(data_column)
                print("Nama Fasilitas : "+data_column[0])
                print("Jenis Jenis : "+data_column[1])
                print("== Masukkan Data Baru ==")
                new_nama_fasilitas = input("Masukkan Nama Fasilitas Baru (Enter untuk skip) : ") or data[1]
                print(data_jenis)
                new_id_jenis_fasilitas = int(input("Masukkan ID Jenis (Enter untuk skip) : ") or str(data[2]))
                values = [new_nama_fasilitas, new_id_jenis_fasilitas]
                model.update_data(table=tabel_fasilitas, idcolomn=pilih_id, values=values)
                print("\n[Data sudah diperbarui!]")
                req = input('Klik ENTER untuk melanjutkan!')
                core.clear()
                
                
            else:
                print("\n[Data tidak ada!]")
                req = input('Klik ENTER untuk melanjutkan!')
                core.clear()
                # continue
        except ValueError:
            print("\n[Id harus berupa angka saja!]")
            req = input('Klik ENTER untuk melanjutkan!')
            core.clear()
            # continue

    else:
        core.clear()


def aksi_fasilitas():
    while True:
        core.clear()
        print("[FASILITAS]")
        print("""
Menu :
1. Lihat Fasilitas
2. Tambah Fasilitas
3. Update Fasilitas
4. Hapus Fasiltias
9. Kembali
""")

        input_user = input("Pilih Menu : ")

        match input_user:
            case "1":
                lihat_fasilitas()
                req = input('Klik ENTER untuk melanjutkan...')
                core.clear()
            case "2":
                tambah_fasilitas(tabel_fasilitas, tabel_jenis)
                core.clear()
            case "3":
                update_fasilitas(tabel_fasilitas, tabel_jenis)
                core.clear()
            case "4":
                hapus_fasilitas(tabel_fasilitas,tabel_status_fasilitas)
                core.clear()
            case "9":
                core.clear()
                main.mainmenu()

if __name__ == "__main__":
    aksi_fasilitas()
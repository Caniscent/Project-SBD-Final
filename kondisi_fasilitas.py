import model
import core
import main
import connection

table="status_fasilitas"

def read_join(columnid=None):
    conn, cur = connection.connect()
    column = model.column_data(table=table, idenable=1)

    query_join = f"""
SELECT sf.id_status_fasilitas, f.nama_fasilitas, s.nama_status, u.nama_users, sf.keterangan 
FROM status_fasilitas sf
JOIN fasilitas f ON f.id_fasilitas = sf.fasilitas_id
JOIN status s ON s.id_status = sf.status_id
JOIN users u ON u.id_users = sf.users_id
"""
    
    if columnid:
        query = f"{query_join} WHERE {column[0]} = {columnid}"
        cur.execute(query, (columnid))
        result = cur.fetchone()
    else:
        query = f"{query_join} ORDER BY id_status_fasilitas ASC"
        cur.execute(query)
        result = cur.fetchall()
        
    cur.close()
    conn.close()
    return result

def aksi_kondisi_fasilitas():
     while True:
        core.clear()
        print('''
[Pendataan Kondisi Fasilitas]
1. Lihat Kondisi Fasilitas
2. Tambah Kondisi fasilitas
3. Perbarui Kondisi Fasilitas
4. Hapus Kondisi Fasilitas
9. Kembali
    ''')
        kondisi = input("Masukkan nomor: ")
        match kondisi:
            case '1':
                data = read_join()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {str(keterangan):<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")

                req = input("Klik ENTER untuk melanjutkan...")

            case '2':
                while True:
                    fasilitas = model.read_data(table="fasilitas")
                    if fasilitas:
                        print(f"{'ID':<5} {'Nama Fasilitas':<15} {'Jenis Fasilitas':<5}")
                        print("-" * 37)
                        for row in fasilitas:
                            id_fasilitas, nama_fasilitas, jenis_fasilitas_id = row
                            print(f"{id_fasilitas:<5} {nama_fasilitas:<15} {jenis_fasilitas_id:<5}")
                    else:
                        print("[Tidak ada data fasilitas yang tersedia]")
                        enter = input()
                        core.clear()
                        break
                    id_fasilitas = input("Masukkan ID Fasilitas sesuai data diatas: ")

                    status = model.read_data(table="status")
                    if status:
                        print(f"{'ID':<5} {'Status':<5}")
                        print("-" * 17)
                        for row in status:
                            id_status, nama_status = row
                            print(f"{id_status:<5} {nama_status:<5}")
                    else:
                        print("[Tidak ada data status yang tersedia]")
                        enter = input()
                        core.clear()
                        break
                    id_status = input("Masukkan ID Status sesuai data diatas: ")

                    users = model.read_data(table="users")
                    if users:
                        print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                        print("-" * 110)
                        for row in users:
                            id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                            print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                    else:
                        print("[Tidak ada data user yang tersedia]")
                        enter = input()
                        core.clear()
                        break
                    id_users = input("Masukkan ID User sesuai data diatas: ")

                    keterangan = input("Masukkan Keterangan: ")

                    if not (id_fasilitas and id_status and id_users):
                        print('\n[ DATA TIDAK LENGKAP ]')
                        print('Klik ENTER untuk melanjutkan!')
                        enter = input()
                        core.clear()
                        break

                    id_fasilitas = int(id_fasilitas)
                    id_status = int(id_status)
                    id_users = int(id_users)

                    data = model.read_data(table="status_fasilitas")
                    data_ada = [cek[1] for cek in data]
                    # for cek in data[1:]:
                    #     data_ada.append(cek[1])
                    if id_fasilitas in data_ada:
                        print('\n[ KONDISI UNTUK FASILITAS INI SUDAH ADA ]')
                        print('Klik ENTER untuk melanjutkan!')
                        enter = input()
                        core.clear()
                        break

                    if keterangan:
                        values = [id_fasilitas,id_status,id_users,keterangan]
                    else: 
                        values = [id_fasilitas,id_status,id_users, None]
                    model.create_data(table = "status_fasilitas", values= values)
                    print("\n[ DATA BERHASIL DITAMBAHKAN ]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    break
                
            case '3':
                while True:
                    data = read_join()
                    if data:
                        print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                        print("-" * 90)
                        for row in data:
                            id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                            print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {str(keterangan):<30}")
                    else:
                        print("Tidak ada data kondisi fasilitas yang tersedia.")
                        req = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        break
                    id_column = input(f"pilih ID Status Fasilitas yang akan diperbarui: ")
                    if id_column:
                        try:    
                            id_column = int(id_column)
                            if any(id_status_fasilitas == id_column for id_status_fasilitas, _, _, _, _ in data):
                                read = model.read_data(table=table,columnid=id_column)
                                print(f"""
Data saat ini:
ID Status Fasilitas: {read[0]}
Nama Fasilitas: {read[1]}
Status: {read[2]}
Nama User: {read[3]}
Keterangan: {read[4]}\n
""")
                                print("Perbarui Data Kondisi")
                                print('-'*37)
                                fasilitas = model.read_data(table="fasilitas")
                                if fasilitas:
                                    print(f"{'ID':<5} {'Nama Fasilitas':<15} {'Jenis Fasilitas':<5}")
                                    print("-" * 37)
                                    for row in fasilitas:
                                        id_fasilitas, nama_fasilitas, jenis_fasilitas_id = row
                                        print(f"{id_fasilitas:<5} {nama_fasilitas:<15} {jenis_fasilitas_id:<5}")
                                else:
                                    print("[Tidak ada data fasilitas yang tersedia]")
                                    req = input('Klik ENTER untuk melanjutkan!')
                                    core.clear()
                                    break
                                id_fasilitas = input("Perbarui ID fasilitas sesuai data diatas: ") or read[1]

                                status = model.read_data(table="status")
                                if status:
                                    print(f"{'ID':<5} {'Status':<5}")
                                    print("-" * 17)
                                    for row in status:
                                        id_status, nama_status = row
                                        print(f"{id_status:<5} {nama_status:<5}")
                                else:
                                    print("[Tidak ada data status yang tersedia]")
                                    req = input('Klik ENTER untuk melanjutkan!')
                                    core.clear()
                                    break
                                id_status = input("Perbarui ID Status sesuai data diatas: ") or read[2]

                                users = model.read_data(table="users")
                                if users:
                                    print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                                    print("-" * 110)
                                    for row in users:
                                        id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                                        print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                                else:
                                    print("[Tidak ada data user yang tersedia]")
                                    req = input('Klik ENTER untuk melanjutkan!')
                                    core.clear()
                                    break
                                id_users = input("Perbarui ID User sesuai data diatas: ") or read[3]

                                keterangan = input("Perbarui Keterangan: ") or read[4]

                                if keterangan:
                                    values = [id_fasilitas,id_status,id_users,keterangan]
                                else:
                                    values = [id_fasilitas,id_status,id_users,None]
                                model.update_data(table=table,idcolomn=id_column,values=values)
                                # read = model.read_data(table=table)
                                print("\n[Data sudah diperbarui]")
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

                    

            case '4':
                while True:
                    data = read_join()
                    if data:
                        print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                        print("-" * 90)
                        for row in data:
                            id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                            print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {str(keterangan):<30}")
                    else:
                        print("Tidak ada data kondisi fasilitas yang tersedia.")
                        req = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        break
                    id_column = input(f"pilih ID Status Fasilitas yang akan dihapus: ")
                    if id_column:
                        try:    
                            id_column = int(id_column)
                            if any(id_status_fasilitas == id_column for id_status_fasilitas, _, _, _, _ in data):
                                read_column = read_join(columnid=id_column)
                                print(f"ID Status Fasilitas: {read_column[0]}")
                                print(f"Nama Fasilitas : {read_column[1]}")
                                print(f"Status: {read_column[2]}")
                                print(f"Nama User: {read_column[3]}")
                                user = input("Yakin ingin menghapus?(Y/n) ")
                                if user.lower() == 'y':
                                    model.delete_data(table=table,idcolumn=id_column)
                                    print("\n[Data sudah dihapus]")
                                    req = input('Klik ENTER untuk melanjutkan!')
                                    core.clear()
                                    break
                                else:
                                    print("\n[Data tidak jadi dihapus]")
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
                    

            case '9':
                core.clear()
                main.mainmenu() 


if __name__ == "__main__":
    aksi_kondisi_fasilitas()
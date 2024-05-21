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
ORDER BY sf.id_status_fasilitas
"""
    
    if columnid:
        query = f"{query_join} WHERE {column[0]} = %s"
        cur.execute(query, (columnid,))
        result = cur.fetchone()
    else:
        query = query_join
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
                core.clear()
                data = read_join()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {keterangan:<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")

                req = input("Klik ENTER untuk melanjutkan...")

            case '2':
                core.clear()
                fasilitas = model.read_data(table="fasilitas")
                if fasilitas:
                    print(f"{'ID':<5} {'Nama Fasilitas':<15} {'Jenis Fasilitas':<5}")
                    print("-" * 37)
                    for row in fasilitas:
                        id_fasilitas, nama_fasilitas, jenis_fasilitas_id = row
                        print(f"{id_fasilitas:<5} {nama_fasilitas:<15} {jenis_fasilitas_id:<5}")
                else:
                    print("Tidak ada data fasilitas yang tersedia.")
                id_fasilitas = input("Masukkan ID Fasilitas sesuai data diatas: ")

                status = model.read_data(table="status")
                if status:
                    print(f"{'ID':<5} {'Status':<5}")
                    print("-" * 17)
                    for row in status:
                        id_status, nama_status = row
                        print(f"{id_status:<5} {nama_status:<5}")
                else:
                    print("Tidak ada data status yang tersedia.")
                id_status = input("Masukkan ID Status sesuai data diatas: ")

                users = model.read_data(table="users")
                if users:
                    print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                    print("-" * 110)
                    for row in users:
                        id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                        print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                else:
                    print("Tidak ada data user yang tersedia.")
                id_users = input("Masukkan ID User sesuai data diatas: ")

                keterangan = input("Masukkan Keterangan: ")
                values = [id_fasilitas,id_status,id_users,keterangan]
                model.create_data(table = "status_fasilitas", values= values)
            
            case '3':
                core.clear()
                data = read_join()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {keterangan:<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")
                id_column = int(input(f"pilih ID Status Fasilitas yang akan dihapus: "))
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
                fasilitas = model.read_data(table="fasilitas")
                if fasilitas:
                    print(f"{'ID':<5} {'Nama Fasilitas':<15} {'Jenis Fasilitas':<5}")
                    print("-" * 37)
                    for row in fasilitas:
                        id_fasilitas, nama_fasilitas, jenis_fasilitas_id = row
                        print(f"{id_fasilitas:<5} {nama_fasilitas:<15} {jenis_fasilitas_id:<5}")
                else:
                    print("Tidak ada data fasilitas yang tersedia.")
                id_fasilitas = input("Perbarui ID fasilitas sesuai data diatas: ") or read[1]

                status = model.read_data(table="status")
                if status:
                    print(f"{'ID':<5} {'Status':<5}")
                    print("-" * 17)
                    for row in status:
                        id_status, nama_status = row
                        print(f"{id_status:<5} {nama_status:<5}")
                else:
                    print("Tidak ada data status yang tersedia.")
                id_status = input("Perbarui ID Status sesuai data diatas: ") or read[2]

                users = model.read_data(table="users")
                if users:
                    print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                    print("-" * 110)
                    for row in users:
                        id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                        print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                else:
                    print("Tidak ada data user yang tersedia.")
                id_users = input("Perbarui ID User sesuai data diatas: ") or read[3]

                keterangan = input("Perbarui Keterangan: ") or read[4]

                values = [id_fasilitas,id_status,id_users,keterangan]
                model.update_data(table=table,idcolomn=id_column,values=values)
                read = model.read_data(table=table)
                data = read_join()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {keterangan:<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")

            case '4':
                core.clear()
                data = read_join()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {keterangan:<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")
                id_column = int(input(f"pilih ID Status Fasilitas yang akan dihapus: "))
                read_column = read_join(columnid=id_column)
                print(f"ID Status Fasilitas: {read_column[0]}")
                print(f"Nama Fasilitas : {read_column[1]}")
                print(f"Status: {read_column[2]}")
                print(f"Nama User: {read_column[3]}")
                user = input("Yakin ingin menghapus?(Y/n) ")
                if user.lower() == 'y':
                    model.delete_data(table=table,idcolomn=id_column)
                else:
                    print("Data tidak jadi dihapus")

                data = read_join()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {keterangan:<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")

            case '9':
                core.clear()
                main.mainmenu() 


if __name__ == "__main__":
    aksi_kondisi_fasilitas()
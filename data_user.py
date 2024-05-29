import model
import core
import main
import hashlib

table = "users"
table_foreign = "status_fasilitas"

def aksi_users():
    while True:
        core.clear()
        print('''
[Pendataan Admin]
1. Lihat Data User
2. Tambah User
3. Perbarui Data User
4. Hapus Data User
9. Kembali
    ''')
        admin = input("Masukkan nomor: ")
        match admin:
            case '1':
                data = model.read_data(select="u.id_users, u.nama_users, u.username, u.password, u.no_telepon_users, ju.nama_jenis_users",
                                       table="users u",
                                       orderby="id_users",
                                       join_tables=["jenis_users ju"],
                                       join_conditions=["u.jenis_users_id = ju.id_jenis_users"])
                if data:
                    print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                    print("-" * 110)
                    for row in data:
                        id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                        print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                else:
                    print("Tidak ada data user yang tersedia.")

                req = input("Klik ENTER untuk kembali...")

            case '2':
                while True:
                    nama_users = input("Masukkan Nama Lengkap: ")
                    username = input("Masukkan Username: ")
                    password = input("Masukkan Password: ")
                    no_telepon_users = input("Masukkan Nomor Telepon: ")
                    jenis_users = input("Masukkan Role User(1=Owner/2=Admin): ")

                    if not (nama_users and username and password and no_telepon_users and jenis_users):
                        print('\n[ DATA TIDAK LENGKAP ]')
                        print('Klik ENTER untuk melanjutkan!')
                        enter = input()
                        core.clear()
                        break
                    jenis_users = int(jenis_users)
                    hashed_password = hashlib.md5(password.encode()).hexdigest()
                    data = model.read_data(table="users")  
                    data_ada = []
                    for cek in data[2:]:
                        data_ada.append(cek[2])
                        if username in data_ada:
                            print('\n[ USERNAME INI SUDAH ADA ]')
                            print('Klik ENTER untuk melanjutkan!')
                            enter = input()
                            core.clear()
                            break
                    values = [nama_users,username,hashed_password,no_telepon_users,jenis_users]
                    model.create_data(table = "users", values= values)
                    print("\n[ DATA BERHASIL DITAMBAHKAN ]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    break
                

            case '3':
                while True:
                    data = model.read_data(select="u.id_users, u.nama_users, u.username, u.password, u.no_telepon_users, ju.nama_jenis_users",
                                       table="users u",
                                       orderby="id_users",
                                       join_tables=["jenis_users ju"],
                                       join_conditions=["u.jenis_users_id = ju.id_jenis_users"])
                    if data:
                        print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                        print("-" * 110)
                        for row in data:
                            id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                            print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                    else:
                        print("Tidak ada data user yang tersedia.")

                    id_column = input(f"Masukkan ID {table} yang akan diperbarui: ")
                    if id_column:
                        try:    
                            id_column = int(id_column)
                            if any(id_users == id_column for id_users, _, _, _, _, _ in data):
                                data_column = model.read_data(table=table,columnid=str(id_column))
                                print(f"""Data saat ini:")
ID Users: {data_column[0]}
Nama Lengkap: {data_column[1]}
Username: {data_column[2]}
Password: {data_column[3]}
No Telepon Users: {data_column[4]}
Jenis Users Id: {data_column[5]}
""")

                                print('-'*30)
                                nama_users = input("Nama Users: ") or data_column[1]
                                username = input("Username: ") or data_column[2]
                                password = input("Password: ") or data_column[3]
                                no_telepon_users = input("Nomor Telepon: ") or data_column[4]
                                print("1. Owner\n2. Admin")
                                jenis_users_id = int(input("Jenis Fasilitas(1/2): ") or data_column[5])
                                hashed_password = hashlib.md5(password.encode()).hexdigest()
                                values = [nama_users,username,hashed_password,no_telepon_users,jenis_users_id]
                                model.update_data(table=table,idcolomn=id_column,values=values)
                                # read = model.read_data(table=table)
                                print("\n[User sudah diperbarui]")
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
                    data = model.read_data(table=table,orderby="id_users")
                    if data:
                        print(f"{'ID':<5} {'Nama User':<30} {'Username':<10} {'Password':<35} {'Nomor Telepon':<15} {'Jenis User':<5}")
                        print("-" * 110)
                        for row in data:
                            id_users, nama_users, username, password, no_telepon_users, jenis_users_id = row
                            print(f"{id_users:<5} {nama_users:<30} {username:<10} {password:<35} {no_telepon_users:<15} {jenis_users_id:<5}")
                    else:
                        print("[Tidak ada data user yang tersedia]")

                    id_column = input(f"Pilih ID {table} yang akan dihapus: ")
                    if id_column:
                        try:
                            id_column = int(id_column)
                            if any(id_users == id_column for id_users, _, _, _, _, _ in data):
                                data_column = model.read_data(table=table,columnid=id_column)
                                print(f"""
ID Users: {data_column[0]}
Nama Lengkap: {data_column[1]}
Username: {data_column[2]}
                                """)
                                user = input("Yakin ingin menghapus?(Y/n) ")
                                if user.lower() == 'y' and data_column[2] != 'nahel':
                                    model.delete_data(table=table,idcolumn=id_column,foreign_key="users_id",foreign_table=table_foreign)
                                    print('\n[User sudah dihapus]')
                                    req = input('Klik ENTER untuk melanjutkan!')
                                    break
                                elif user.lower() == 'y'and data_column[2] == 'nahel':
                                    print('\n[ OWNER UTAMA TIDAK BOLEH DIHAPUS! ]')
                                    req = input('Klik ENTER untuk melanjutkan!')
                                    break
                                else:
                                    print("\n[User tidak jadi dihapus]")
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
                        continue
                    
                
            case '9':
                core.clear()
                main.mainmenu() 
                    


if __name__ == "__main__":
    aksi_users()
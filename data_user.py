import model
import core
import main
import hashlib


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
                data = model.read_data(table="users",orderby="id_users")
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
                nama_users = input("Masukkan Nama Lengkap: ")
                username = input("Masukkan Username: ")
                password = input("Masukkan Password: ")
                no_telepon_users = input("Masukkan Nomor Telepon: ")
                jenis_users = int(input("Masukkan Role User(1=Owner/2=Admin): "))
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                values = [nama_users,username,hashed_password,no_telepon_users,jenis_users]
                model.create_data(table = "users", values= values)

            case '3':
                table = "users"
                data = model.read_data(table=table)
                for i in data:
                    print(i)

                id_column = int(input("Masukkan ID Users: "))
                data_column = model.read_data(table=table,columnid=str(id_column))
                print(f"""Data saat ini:")
ID Users: {data_column[0]},
Nama Lengkap: {data_column[1]},
Username: {data_column[2]},
Password: {data_column[3]},
No Telepon Users: {data_column[4]},
Jenis Users Id: {data_column[5]}
                """)

                print('-'*30)
                nama_users = input("Nama Users: ") or data[1]
                username = input("Username: ") or data[2]
                password = input("Password: ") or data[3]
                no_telepon_users = input("Nomor Telepon: ") or data[4]
                print("1. Owner\n2. Admin")
                jenis_users_id = int(input("Jenis Fasilitas(1/2): ") or data[5])
                values = [nama_users,username,password,no_telepon_users,jenis_users_id]
                model.update_data(table=table,idcolomn=id_column,values=values)
                read = model.read_data(table=table)
                for i in read:
                    print(i)
            
            case '4':
                table = "users"
                data = model.read_data(table=table)
                for i in data:
                    print(i)

                id_column = int(input(f"Pilih ID {table} yang akan dihapus: "))
                data_column = model.read_data(table=table,columnid=id_column)
                print(f"""ID Users: {data_column[0]},
Nama Lengkap: {data_column[1]},
Username: {data_column[2]}
                """)
                user = input("Yakin ingin menghapus?(Y/n) ")
                if user.lower() == 'y':
                    model.delete_data(table=table,idcolumn=id_column)
                else:
                    print("Data tidak jadi dihapus")

                read = model.read_data(table=table)
                for i in read:
                    print(i)
            
            case '9':
                core.clear()
                main.mainmenu() 
                


if __name__ == "__main__":
    aksi_users()
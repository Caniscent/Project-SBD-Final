import connection
import model
import core
import main
import hashlib


def aksi_admin():
    while True:
        core.clear()
        print('''
1. Read
2. Create
3. Update
4. Delete
9. Kembali
    ''')
        admin = input("Masukkan nomor: ")
        match admin:
            case '1':
                kon = model.read_data(table="users",orderby="id_users")
                for i in kon:
                    print(i)
                req = input("Klik ENTER untuk melanjutkan...")
                core.clear()
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
                # update = f"UPDATE mata_kuliah SET nama_mata_kuliah = %s, sks = %s, semester_id = %s"
                # read_matkul(cursor=cursor)

                id_users = input("Masukkan Id dari Users yang ingin di update: ")
                select_query = f"SELECT * FROM users WHERE id_users = %s"
                connection.cursor.execute(query=select_query, vars=(id_users))
                data = connection.cursor.fetchone()

                if data:
                    print("Data saat ini:")
                    print(f"Id users saat ini: {data[0]}")
                    print(f"Nama users saat ini: {data[1]}")
                    print(f"Username saat ini: {data[2]}")
                    print(f"Password saat ini: {data[3]}")
                    print(f"Nomor telepon saat ini: {data[4]}")
                    print(f"Jenis user saat ini: {data[5]}")

                nama_users = input("Masukkan nama lengkap: ") or data[1]
                username = input("Masukkan username: ") or data[2]
                password = input("Masukkan password: ") or data[3]
                no_telepon_users = input("Masukkan nomor telepon: ") or data[4]
                jenis_users_id = int(input("Masukkan jenis users: ")) or data[5]

                query_update = f"UPDATE users SET nama_users = %s, username = %s, password = %s WHERE id_users = %s"
                connection.cursor.execute(query=query_update, vars=(nama_users, username, password, no_telepon_users, jenis_users_id))


                print(f"Total baris yang diubah: {connection.cursor.rowcount}")
                connection.conn.commit()
                connection.cursor.close()
                connection.conn.close()
            
            case '4':
                table = "users"
                data = model.read_data(table=table)
                for i in data:
                    print(i)

                id_column = int(input(f"Pilih ID {table} yang akan dihapus: "))
                data_column = model.read_data(table=table,columnid=id_column)
                print(f"""ID Fasilitas: {data_column[0]},
                Nama Fasilitas: {data_column[1]}
                Jenis Fasilitas: {data_column[2]}
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
                
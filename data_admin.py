import connection
import model
import core
import main


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
                model.read_data(table="users",orderby="id_users")

            case '2':
                nik_users = int(input("Masukkan NIK: "))
                nama_users = input("Masukkan Nama Lengkap: ")
                username = input("Masukkan Username: ")
                password = input("Masukkan Password: ")
                no_telepon_users = input("Masukkan Nomor Telepon: ")
                jenis_users = int(input("Masukkan Role User(1=Owner/2=Admin): "))
                values = [nik_users,nama_users,username,password,no_telepon_users,jenis_users]
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
                connection.read_users(cursor=connection.cursor)
                id_users = input("Masukkan Id Users yang ingin di hapus: ")
                query_delete = f"DELETE FROM users WHERE id_users = {id_users}"
                connection.cursor.execute(query=query_delete)

                print(f"Total baris yang diubah: {connection.cursor.rowcount}")
                connection.conn.commit()
                connection.cursor.close()
                connection.conn.close()
            
            case '9':
                core.clear()
                main.mainmenu() 
                
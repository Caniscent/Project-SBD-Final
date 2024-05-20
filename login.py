import core
import getpass
import hashlib
import model

SESSION_GLOBAL = {}
   
     
def login():
    #Temp variabel
    data_admin = []
    # Membaca database data_admin
    data = model.read_data(select="username, password, jenis_users_id",table="users")
    # Convert database csv ke dictionary
    for i in data:
        data_admin.append({"username": i[0], "password": i[1]})

    #Count kesempatan untuk login
    percobaan = 3
    sesi_login = False
    
    # Main Program
    while percobaan > 0 and not sesi_login:
        # Menampilkan UI CLI dari login session
        # with open('ui/login.txt','r') as login_ui:
        #     print(login_ui.read())
        # Meminta input dari user berupa username dan password
        username = input("| Username: ")
        password = getpass.getpass(prompt="| Password: ")

        hashed_password = hashlib.md5(password.encode()).hexdigest()

        

        # Validasi input username dan password terhadap database
        for user in data_admin:
            # Kondisi benar jika input sesuai dengan database
            if username == user['username'] and hashed_password == user['password'] and user['jenis_users_id']:
                # UI Login Berhasil
                salam = f"Selamat Datang {username.title()}"
                print('+' + '='*83 + '+')
                print('|' + '[ LOGIN SUCCESSFUL ]'.center(83) + '|')
                print('|' + salam.center(83) + '|')
                print('+' + '='*83 + '+')
                # setelah masuk, sesi login true
                sesi_login = True
                global SESSION_GLOBAL
                SESSION_GLOBAL = user
                # Pause sebelum di clear
                req = input("| Klik ENTER untuk melanjutkan... ")
                core.clear()
                break

            if username == user['username'] and hashed_password == user['password'] and user['jenis_users_id']:
                print('yahaha gak bisa login')
        # -
        if not sesi_login:
            # UI Login Gagal
            print('+' + '='*83 + '+')
            print('|' + '[ LOGIN FAILED ]'.center(83) + '|')
            print('|' + 'Username atau Password salah!'.center(83) + '|')
            print('+' + '='*83 + '+')
            percobaan -= 1
            #  - 
            if percobaan == 0 and not sesi_login:
                # UI Login gagal
                print('+' + '='*83 + '+')
                print('|' + '[ LOGIN SESSION ATTEMPT OUT ]'.center(83) + '|')
                print('|' + 'Anda telah melebihi batas percobaan login, Silahkan jalankan ulang program!'.center(83) + '|')
                print('+' + '='*83 + '+')
                # Keluar dari program
                exit()
            # Melanjutkan percobaan login
            else:
                req = input("| Klik ENTER untuk melanjutkan... ")
                core.clear()
                
                

if __name__ == "__main__":
    login()
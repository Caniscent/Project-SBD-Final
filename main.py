import core
import login
import data_user
import penghuni
import kamar
import fasilitas
import fasilitas_kamar
import kondisi_fasilitas
import pembayaran

def mainmenu():
    while True:
        core.clear()
        print('''
[Owner Menu]
1. Pendataan Admin
2. Pendataan Penyewaan
3. Pendatan Penghuni
4. Pendataan Fasilitas
5. Ubah Kondisi Fasilitas
6. Pendataan Kamar
7. Pendataan Fasilitas Kamar
9. Logout
0. Keluar
        ''')
        menu = input("Mainmenu: ")
        match menu:
            case '1':
                data_user.aksi_users()
            case '2':
                pembayaran.aksi_pembayaran()    
            case '3':
                penghuni.aksi_penghuni()
            case '4':
                fasilitas.aksi_fasilitas()
            case '5':
                kondisi_fasilitas.aksi_kondisi_fasilitas()
            case "6":
                kamar.aksi_kamar()
            case "7":
                fasilitas_kamar.AksiFasilitasKamar()
            case '9':
                print('Apakah Anda yakin ingin logout? (y/n)')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    login.login() 
                else:
                    core.clear()
            case '0':
                print('|' + 'Apakah Anda yakin ingin keluar? (y/n)')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    exit()
                else:
                    core.clear()
            case _:
                core.clear()

def menuadmin():
    while True:
        core.clear()
        print('''
[Admin Menu]
1. Ubah Kondisi Fasilitas
9. Kembali
0. Keluar
        ''')
        menu = input("Mainmenu: ")
        match menu:
            case '1':
                kondisi_fasilitas.aksi_kondisi_fasilitas()
            case '9':
                print('Apakah Anda yakin ingin logout? (y/n)')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    login.login() 
                else:
                    core.clear()
            case '0':
                print('Apakah Anda yakin ingin keluar? (y/n)')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    exit()
                else:
                    core.clear()
            case _:
                core.clear()

if __name__ == "__main__":
    core.clear()
    # login.login()
    mainmenu()
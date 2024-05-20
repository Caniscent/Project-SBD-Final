import core
import login
import data_admin
import fasilitas

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
9. Kembali
0. Keluar
        ''')
        menu = input("Mainmenu: ")
        match menu:
            case '1':
                data_admin.aksi_admin()
            case '4':
                fasilitas.aksi_fasilitas()
            case '9':
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Apakah Anda yakin untuk kembali ke menu login? (y/n)'.center(83) + '|')
                print('+' + '='*83 + '+')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    login.login() 
                else:
                    core.clear()
            case '0':
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Apakah Anda yakin untuk keluar? (y/n)'.center(83) + '|')
                print('+' + '='*83 + '+')
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
                pass
            case '9':
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Apakah Anda yakin untuk kembali ke menu login? (y/n)'.center(83) + '|')
                print('+' + '='*83 + '+')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    login.login() 
                else:
                    core.clear()
            case '0':
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Apakah Anda yakin untuk keluar? (y/n)'.center(83) + '|')
                print('+' + '='*83 + '+')
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
    login.login()
    mainmenu()
import core
import data_admin


def mainmenu():
    while True:
        core.clear()
        print('''
        1. Tambah Admin
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
            case '9':
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Apakah Anda yakin untuk kembali ke menu login? (y/n)'.center(83) + '|')
                print('+' + '='*83 + '+')
                user = input(f"| > ")
                if user.lower() == 'y' or user.lower() == 'yes':
                    core.clear()
                    continue
                    #login.login() 
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
    mainmenu()
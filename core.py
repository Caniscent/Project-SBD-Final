import os

# fungsi untuk clear console untuk bisa berfungsi di 2 tipe Sistem operasi
def clear():
    if os.name == 'posix': # jika os tipe unix
        os.system('clear')
    elif os.name == 'nt': # jika os tipe windows
        os.system('cls')
    else:
        print("Sistem operasi tidak didukung.")
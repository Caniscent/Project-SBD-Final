import data_admin

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
mainmenu = input("Mainmenu: ")
match mainmenu:
    case '1':
        data_admin.aksi_admin()
    
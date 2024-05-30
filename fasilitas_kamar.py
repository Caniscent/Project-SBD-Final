import connection
import model
import core
import main

# Tabel name identification
TabelFK = "fasilitas_kamar"
TabelKamar = "kamar"
TabelFasilitas = "fasilitas"
# Get column name
ColumnFK = model.column_data(table=TabelFK,idenable=True)
ColumnKamar = model.column_data(table=TabelKamar,idenable=True)
ColumnFasilitas = model.column_data(table=TabelFasilitas,idenable=True)

def CreateFK():
    try:
        # DataKamar = model.read_data(table=TabelKamar)
        # for i in DataKamar:
        #     print(i)
        # Id_Kamar = input("Masukkan ID Kamar: ")
        while True:
            core.clear()
            print("Menambah Data Baru: ")
            data_kamar = model.read_data(table=TabelKamar)
            if data_kamar:
                print(f"{'ID':<5} {'Nomor Kamar':<12} {'Tipe Kamar':<10}")
                print("-" * 36)
                for row in data_kamar:
                    id_kamar, nomor_kamar, tipe_kamar_id = row
                    print(f"{id_kamar:<5} {nomor_kamar:<12} {tipe_kamar_id:<10}")
            else:
                print("[Tidak ada data kamar yang tersedia]")
            id_kamar = input("Masukkan ID kamar: ")
            data_fasilitas = model.read_data(table=TabelFasilitas)
            if data_fasilitas:
                print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Jenis Fasilitas':<5}")
                print("-" * 42)
                for row in data_fasilitas:
                    id_users, nama_fasilitas, jenis_fasilitas = row
                    print(f"{id_users:<5} {nama_fasilitas:<20} {jenis_fasilitas:<5}")
            else:
                print("[Tidak ada data fasilitas yang tersedia]")
            id_fasilitas = input("Masukkan ID Fasilitas: ")
            

            if not (id_kamar and id_fasilitas):
                print('\n[ DATA TIDAK LENGKAP ]')
                print('Klik ENTER untuk melanjutkan!')
                enter = input()
                core.clear()
                break

            id_kamar = int(id_kamar)
            id_fasilitas = int(id_fasilitas)
            
            data = model.read_data(table=TabelFasilitas)  
            data_jenis = [cek[2] for cek in data if cek[2] == '2']
            if id_fasilitas in data_jenis:
                print('\n[ JENIS FASILITAS INI BUKAN FASILITAS KAMAR ]')
                print('Klik ENTER untuk melanjutkan!')
                enter = input()
                core.clear()
                break

            data_fasilitas_id = [cek[1] for cek in data]
            if id_fasilitas in data_fasilitas_id:
                print('\n[ FASILITAS INI SUDAH DIGUNAKAN ]')
                print('Klik ENTER untuk melanjutkan!')
                enter = input()
                core.clear()
                break
            values = [id_kamar, id_fasilitas]
            model.create_data(table = TabelFK, values= values)
            print("\n[ DATA BERHASIL DITAMBAHKAN ]")
            req = input('Klik ENTER untuk melanjutkan!')
            core.clear()
            break

    except Exception as ex:
        print(f"Error: {ex}")


def ReadFK():
    try:
        data = model.read_data(select=f"{TabelFK}.{ColumnFK[0]},{TabelKamar}.{ColumnKamar[1]},{TabelFasilitas}.{ColumnFasilitas[1]}",
                               table=TabelFK,
                               join_tables=[TabelKamar,TabelFasilitas],
                               join_conditions=[f"{TabelKamar}.{ColumnKamar[0]} = {TabelFK}.{ColumnFK[1]}",
                                                f"{TabelFasilitas}.{ColumnFasilitas[0]} = {TabelFK}.{ColumnFK[2]}"])
        if data:
            print(f"{'ID':<5} {'Nomor kamar':<12} {'Nama Fasilitas':<25}")
            print("-" * 35)
            for row in data:
                id_fasilitas_kamar, nomor_kamar, nama_fasilitas = row
                print(f"{id_fasilitas_kamar:<5} {nomor_kamar:<12} {nama_fasilitas:<25}")
        else:
            print("[Tidak ada data user yang tersedia]")
    except Exception as e:
        print(f"Gagal membaca data! Error: {e}")

def UpdateFK():
    try:
        while True:
            core.clear()
            ReadFK()
            read = model.read_data(table=TabelFK)
            id_fk = input("Masukkan ID Fasilitas Kamar: ")
            if id_fk:
                try:    
                    id_column = int(id_fk)
                    if any(read[0] == id_column for read[0], _, _ in read):
                        dataFK = model.read_data(table=TabelFK,columnid=id_column)
                        print("Data saat ini: ")
                        print(f"ID Fasilitas Kamar: {dataFK[0]}")
                        print(f"Nomor Kamar: {dataFK[1]}")
                        print(f"Fasilitas: {dataFK[2]}")
                        print("\nUbah Data: ")
                        data_kamar = model.read_data(table=TabelKamar)
                        if data_kamar:
                            print(f"{'ID':<5} {'ID kamar':<12} {'ID Fasilitas':<25}")
                            print("-" * 35)
                            for row in data_kamar:
                                id_fasilitas_kamar, nomor_kamar, nama_fasilitas = row
                                print(f"{id_fasilitas_kamar:<5} {nomor_kamar:<12} {nama_fasilitas:<25}")
                        else:
                            print("[Tidak ada data kamar yang tersedia]")
                        nomor_kamar = input(f"Masukkan ID Kamar: ") or dataFK[1]
                        
                        data_fasilitas = model.read_data(table=TabelFasilitas)
                        if data_fasilitas:
                            print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Jenis Fasilitas':<5}")
                            print("-" * 42)
                            for row in data_fasilitas:
                                id_users, nama_fasilitas, jenis_fasilitas = row
                                print(f"{id_users:<5} {nama_fasilitas:<20} {jenis_fasilitas:<5}")
                        else:
                            print("Tidak ada data user yang tersedia.")
                        nama_fasilitas = input(f"Masukkan ID Fasilitas: ") or dataFK[2]
                        values = [nomor_kamar,nama_fasilitas]
                        model.update_data(table=TabelFK,idcolomn=id_fk,values=values)
                        req = input("Data berhasil diupdate. Klik Enter untuk melanjutkan...")
                        core.clear()
                        break

                    else:
                        print("Data tidak ada!")
                        re = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        continue
                except ValueError:
                    print("Id harus berupa angka saja!")
                    re = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    continue

            else:
                core.clear()
                continue
        
    except Exception as ex:
        print(f"Error: {ex}")

def DeleteFK():
    try:
        while True:
            core.clear()
            ReadFK()
            read = model.read_data(table=TabelFK)
            id_fk = input("Pilih ID yang ingin dihapus: ")
            if id_fk:
                try:    
                    id_column = int(id_fk)
                    if any(read[0] == id_column for read[0], _, _ in read):
                        data = model.read_data(select=f"{TabelFK}.{ColumnFK[0]},{TabelKamar}.{ColumnKamar[1]},{TabelFasilitas}.{ColumnFasilitas[1]}",
                                table=TabelFK,
                                join_tables=[TabelKamar,TabelFasilitas],
                                join_conditions=[f"{TabelKamar}.{ColumnKamar[0]} = {TabelFK}.{ColumnFK[1]}",
                                                f"{TabelFasilitas}.{ColumnFasilitas[0]} = {TabelFK}.{ColumnFK[2]}"],
                                columnid=id_column)
                        print("[Data yang ingin dihapus]")
                        print(f"ID Fasilitas Kamar: {data[0]}")
                        print(f"Nomor Kamar: {data[1]}")
                        print(f"Nama Fasilitas: {data[2]}")
                        user = input("Apakah anda yakin ingin menghapus?(Y/n) ")
                        if user == 'Y' or user == 'y':
                            model.delete_data(table=TabelFK,idcolumn=id_column)
                            print('\n[Data fasilitas kamar sudah dihapus]')
                            re = input('Klik ENTER untuk melanjutkan!')
                            core.clear()
                            break
                        else:
                            input("\n[Data fasilitas kamar batal dihapus!]")
                            re = input('Klik ENTER untuk melanjutkan!')  
                            core.clear()
                            break
                    else:
                        print("Data tidak ada!")
                        re = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        continue
                except ValueError:
                    print("Id harus berupa angka saja!")
                    re = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    continue

            else:
                core.clear()
                continue
        
    except Exception as ex:
        print(f"Error: {ex}")

def AksiFasilitasKamar():
    try:
        while True:
            core.clear()
            print('''
[Pendataan Fasilitas Kamar]
1. Lihat Data Fasilitas Kamar
2. Tambah Data Fasilitas Kamar
3. Perbarui Data Fasilitas Kamar
4. Hapus Data Fasilitas Kamar
9. Kembali
    ''')
            user = input("Masukkan nomor: ")
            match user:
                case '1':
                    ReadFK()
                    req = input("Klik ENTER untuk melanjutkan...")
                case '2':
                    CreateFK()
                case '3':
                    UpdateFK()
                case '4':
                    DeleteFK()
                case '9':
                    core.clear()
                    main.mainmenu()

    except Exception as ex:
        print(f"Error: {ex}")


if __name__ == "__main__":
    AksiFasilitasKamar()
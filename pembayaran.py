import model
import connection
import datetime
import core
import main
from dateutil.relativedelta import relativedelta

tabel = "pembayaran"
tabel_penghuni = "penghuni" 

def menambah_pembayaran():
    print(f"[Menambah data baru]")
    tanggal_pembayaran = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # tanggal_pembayaran = input("Masukkan tanggal pembayaran (enter untuk today) :" or tanggal_pembayaran)
    lama_sewa = int(input("Masukkan lama sewa (bulan) : "))
    tenggat_pembayaran = datetime.datetime.now() + relativedelta(months=+lama_sewa)
    tenggat_pembayaran = tenggat_pembayaran.strftime('%Y-%m-%d %H:%M:%S')
    penghuni = model.read_data(table=tabel_penghuni)
    if penghuni:
        print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar ID':<5}")
        print("-" * 140)
        for row in penghuni:
            id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk, tanggal_keluar, kamar_id = row
            print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
    else:
        print("[Tidak ada data penghuni yang tersedia]")
    id_penghuni = input("Masukkan ID Penghuni: ")

    if not (tanggal_pembayaran and tenggat_pembayaran and penghuni):
        print('\n[ DATA TIDAK LENGKAP ]')
        print('Klik ENTER untuk melanjutkan!')
        enter = input()
        core.clear()
    
    penghuni = int(penghuni)

    values = [tanggal_pembayaran, tenggat_pembayaran, id_penghuni]
    model.create_data(table=tabel,values=values)
    print("\n[ DATA BERHASIL DITAMBAHKAN ]")
    req = input('Klik ENTER untuk melanjutkan!')
    core.clear()
    

def read_join():
    conn, cur = connection.connect()
    column = model.column_data(table=tabel, idenable=1)

    query_join = f"""
SELECT pem.id_pembayaran, pem.tanggal_pembayaran, pem.tenggat_pembayaran, p.nama_penghuni
from pembayaran pem
join penghuni p on p.id_penghuni = penghuni_id
ORDER BY {column[0]} ASC
"""
    
    cur.execute(query_join)
    result = cur.fetchall()
    
    cur.close()
    conn.close()
    return result


def read_pembayaran():
    data = read_join()
    if data:
        print(f"{'ID':<5} {'Tanggal Pembayaran':<30} {'Tenggat Pembayaran':<30} {'Penghuni':<35}")
        print("-" * 95)
        for row in data:
            id_pembayaran, tanggal_pembayaran, tenggat_pembayaran, penghuni = row
            print(f"{id_pembayaran:<5} {str(tanggal_pembayaran):<30} {str(tenggat_pembayaran):<30} {penghuni:<35}")
    else:
        print("[Tidak ada data yang tersedia]")


def update_pembayaran():
    while True:
        core.clear()
        read_pembayaran()
        read = model.read_data(table=tabel,columnid=id)
        id_column = input("Pilih ID pembayaran yang ingin diupdate: ")
        if id_column:
            try:    
                id_column = int(id_column)
                if any(id_pembayaran == id_column for id_pembayaran, _, _, _ in read):
                    data = model.read_data(table=tabel,columnid=id_column)
                    data_penghuni = model.read_data(table=tabel_penghuni,columnid=data[3])
                    print("Data: ")
                    print(f"ID Pembayaran: {data[0]}")
                    print(f"Tanggal Pembayaran: {data[1]}")
                    print(f"Tenggat Pembayaran: {data[2]}")
                    print(f"Penghuni: {data_penghuni[2]}")
                    print('-'*30)
                    print(f"Update data: ")
                    tanggal_pembayaran = str(input("Masukkan tanggal pembayaran(YYYY/MM/DD HH:MM:SS): ") or data[1])
                    tenggat_pembayaran = str(input("Masukkan tenggat pembayaran(YYYY/MM/DD HH:MM:SS): ") or data[2])
                    print(f"Data Penghuni: ")
                    penghuni = model.read_data(table=tabel_penghuni,orderby="id_penghuni") 
                    if penghuni:
                        print(f"{'ID':<5} {'NIK Penghuni':<20} {'Nama Penghuni':<30} {'Nomor Telepon Penghuni':<25} {'Tanggal Masuk':<25} {'Tanggal keluar':<20} {'Kamar ID':<5}")
                        print("-" * 140)
                        for row in penghuni:
                            id_penghuni, nik_penghuni, nama_penghuni, no_telepon_penghuni, tanggal_masuk, tanggal_keluar, kamar_id = row
                            print(f"{id_penghuni:<5} {nik_penghuni:<20} {nama_penghuni:<30} {no_telepon_penghuni:<25} {str(tanggal_masuk):<25} {str(tanggal_keluar):<20} {kamar_id:<5}")
                    else:
                        print("[Tidak ada data penghuni yang tersedia]")
                    penghuni_id = str(input("Masukkan ID Penghuni: ") or data[3])
                    values = [tanggal_pembayaran,tenggat_pembayaran,penghuni_id]
                    model.update_data(table=tabel,idcolomn=id_column,values=values)
                    req = input("Data berhasil diupdate. Klik Enter untuk melanjutkan...")
                    core.clear()
                    break

                else:
                    print("\n[Data tidak ada!]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    continue
            except ValueError:
                print("\n[Id harus berupa angka saja!]")
                req = input('Klik ENTER untuk melanjutkan!')
                core.clear()
                continue

        else:
            core.clear()
            continue
    

def hapus_pembayaran():
    while True:
        core.clear()
        read_pembayaran()
        read = model.read_data(table=tabel)
        kolom = input("Pilih ID yang ingin dihapus: ")
        if kolom:
            try:    
                id_column = int(kolom)
                if any(id_pembayaran == id_column for id_pembayaran, _, _, _ in read):
                    data = model.read_data(table=tabel,columnid=kolom)
                    column = model.column_data(table=tabel,idenable=True)
                    print("[Data yang ingin dihapus]")
                    print(f"ID Pembayaran: {data[0]}")
                    print(f"Tanggal Pembayaran: {data[1]}")
                    print(f"Tenggat Pembayaran: {data[2]}")
                    print(f"ID Penghuni: {data[3]}")
                    req = input("Apakah anda yakin ingin menghapus? (Y/n)")
                    if req == 'Y' or req == 'y':
                        model.delete_data(table=tabel,idcolumn=id_column)
                        print('\n[Data penyewaan sudah dihapus]')
                        req = input('Klik ENTER untuk melanjutkan!')
                        core.clear()
                        break
                    else:
                        input("\n[Data penyewaan batal dihapus!]")
                        req = input('Klik ENTER untuk melanjutkan!')  
                        core.clear()
                        break        

                else:
                    print("\n[Data tidak ada!]")
                    req = input('Klik ENTER untuk melanjutkan!')
                    core.clear()
                    continue
            except ValueError:
                print("\n[Id harus berupa angka saja!]")
                req = input('Klik ENTER untuk melanjutkan!')
                core.clear()
                continue

        else:
            core.clear()
            continue

        


def aksi_pembayaran():
    while True:
        core.clear()
        print("[PEMBAYARAN]")
        print("""
Menu :
1. Lihat Penyewaan
2. Tambah Penyewaan
3. Perbarui Penyewaan
4. Hapus Penyewaan
5. Kembali
""")

        input_user = input("Pilih Menu : ")

        match input_user:
            case "1":
                read_pembayaran()
                req = input("Klik ENTER untuk melanjutkan...")
            case "2":
                menambah_pembayaran()
            case "3":
                update_pembayaran()
            case "4":
                hapus_pembayaran()
            case "5":
                core.clear()
                main.mainmenu()

if __name__ == "__main__":
    aksi_pembayaran()
    
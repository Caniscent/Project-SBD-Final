import model
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
    for i in penghuni:
        print(i)
    id_penghuni = input("Masukkan ID Penghuni: ")
    values = [tanggal_pembayaran, tenggat_pembayaran, id_penghuni]
    model.create_data(table=tabel,values=values)

def read_pembayaran():
    column = model.column_data(table=tabel,idenable=True)
    data = model.read_data(table=tabel)
    print(column)
    for i in data:
        print(i)

def update_pembayaran():
    pass

def hapus_pembayaran():
    read_pembayaran()
    kolom = input("Pilih ID yang ingin dihapus: ")
    data = model.read_data(table=tabel,columnid=kolom)
    data2 = model.read_data(table=tabel,columnid=data[3])
    column = model.column_data(table=tabel,idenable=True)
    x = print("[Data yang ingin dihapus]")
    print(f"ID Pembayaran: {data[0]}")
    print(f"Tanggal Pembayaran: {data[1]}")
    print(f"Tenggat Pembayaran: {data[2]}")
    print(f"Penghuni_id: {data2[1]}")
    req = input("Apakah anda yakin ingin menghapus? (Y/n)")
    if req == 'Y' or req == 'y':
        model.delete_data(table=tabel,idcolumn=kolom)
    else:
        req = input("Data gagal dihapus!")

    


def aksi_pembayaran():
    core.clear()
    while True:
        print("PEMBAYARAN]")
        print("""Menu :
        1. Lihat Pembayaran
        2. Tambah Pembayaran
        3. Update Pembayaran
        4. Hapus Pembayaran
        5. Kembali
        """)

        input_user = input("Pilih Menu : ")

        match input_user:
            case "1":
                core.clear()
                read_pembayaran()
            case "2":
                menambah_pembayaran()
            case "3":
                core.clear()
                update_pembayaran()
            case "4":
                core.clear()
                hapus_pembayaran()
            case "5":
                core.clear()
                main.mainmenu()

if __name__ == "__main__":
    aksi_pembayaran()
    
import model

tabel = "pembayaran"
tabel_penghuni = "penghuni"

def menambah_pembayaran():
    print(f"[Menambah data baru]")
    tanggal_pembayaran = input("Masukkan tanggal pembayaran: ")
    tenggat_pembayaran = input("Masukkan tenggat pembayaran: ")
    penghuni = model.read_data(table=tabel_penghuni)
    for i in penghuni:
        print(i)
    id_penghuni = input("Masukkan ID Penghuni: ")
    values = [tanggal_pembayaran,tenggat_pembayaran,id_penghuni]
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
    pass

def aksi_pembayaran():
    menambah_pembayaran()

if __name__ == "__main__":
    # column = model.column_data(table=tabel)
    # print(column)
    aksi_pembayaran()
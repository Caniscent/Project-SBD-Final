import model
import core
import main
import connection

def aksi_kondisi_fasilitas():
     while True:
        core.clear()
        print('''
[Pendataan Kondisi Fasilitas]
1. Lihat Kondisi Fasilitas
2. Tambah Kondisi fasilitas
3. Perbarui Kondisi Fasilitas
4. Hapus Kondisi Fasilitas
9. Kembali
    ''')
        kondisi = input("Masukkan nomor: ")
        match kondisi:
            case '1':
                conn, cur = connection.connect()
                query = f"""
SELECT sf.id_status_fasilitas, f.nama_fasilitas, s.nama_status, u.nama_users, sf.keterangan 
FROM status_fasilitas sf
JOIN fasilitas f ON f.id_fasilitas = sf.fasilitas_id
JOIN status s ON s.id_status = sf.status_id
JOIN users u ON u.id_users = sf.users_id
"""
                cur.execute(query)
                data = cur.fetchall()
                if data:
                    print(f"{'ID':<5} {'Nama Fasilitas':<20} {'Status':<15} {'User':<30} {'Keterangan':<30}")
                    print("-" * 90)
                    for row in data:
                        id_status_fasilitas, nama_fasilitas, nama_status, nama_users, keterangan = row
                        print(f"{id_status_fasilitas:<5} {nama_fasilitas:<20} {nama_status:<15} {nama_users:<30} {keterangan:<30}")
                else:
                    print("Tidak ada data kondisi fasilitas yang tersedia.")

                req = input("Klik ENTER untuk melanjutkan...")

                cur.close()
                conn.close()

            case '2':
                pass
            
            case '3':
                pass

            case '4':
                pass

            case '9':
                core.clear()
                main.mainmenu() 


if __name__ == "__main__":
    aksi_kondisi_fasilitas()
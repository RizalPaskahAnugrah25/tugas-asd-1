class TokoPakaian:
    def __init__(self):
        self.pakaian = {
            'Hoodie Hitam': {'berat': '330gsm', 'harga': 300000, 'stok': 10},
            'Kaos Putih': {'berat': 'polos', 'harga': 80000, 'stok': 20},
            'Kemeja Hitam': {'berat': 'polos', 'harga': 120000, 'stok': 15},
            'Celana Denim Jeans': {'berat': 'Jeans', 'harga': 200000, 'stok': 12},
            'Crewneck': {'berat': 'standar', 'harga': 150000, 'stok': 18}
        }

    def tambah_pakaian(self, nama, berat, harga, stok):
        self.pakaian[nama] = {'berat': berat, 'harga': harga, 'stok': stok}
        print(f"Pakaian {nama} berhasil ditambahkan.")

    def tampilkan_pakaian(self):
        print("Daftar Pakaian:")
        for nama, detail in self.pakaian.items():
            print(f"{nama} - Berat: {detail['berat']}, Harga: {detail['harga']}, Stok: {detail['stok']}")

    def ubah_pakaian(self, nama, field, nilai_baru):
        if nama in self.pakaian:
            if field in self.pakaian[nama]:
                self.pakaian[nama][field] = nilai_baru
                print(f"{field} pada pakaian {nama} berhasil diubah.")
            else:
                print(f"Field {field} tidak valid.")
        else:
            print(f"Pakaian {nama} tidak ditemukan.")

    def hapus_pakaian(self, nama):
        if nama in self.pakaian:
            del self.pakaian[nama]
            print(f"Pakaian {nama} berhasil dihapus.")
        else:
            print(f"Pakaian {nama} tidak ditemukan.")

# Contoh penggunaan
toko_pakaian = TokoPakaian()

# Menampilkan daftar pakaian
toko_pakaian.tampilkan_pakaian()

# Menambahkan pakaian baru
toko_pakaian.tambah_pakaian("Jaket Kulit", "berat", 500000, 8)

# Menampilkan daftar pakaian setelah penambahan
toko_pakaian.tampilkan_pakaian()

# Mengubah harga Kaos Putih
toko_pakaian.ubah_pakaian("Kaos Putih", "harga", 90000)

# Menampilkan daftar pakaian setelah perubahan
toko_pakaian.tampilkan_pakaian()

# Menghapus Kemeja Hitam dari daftar
toko_pakaian.hapus_pakaian("Kemeja Hitam")

# Menampilkan daftar pakaian setelah penghapusan
toko_pakaian.tampilkan_pakaian()

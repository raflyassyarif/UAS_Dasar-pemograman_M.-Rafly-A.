class KasirMaterial:
    def __init__(self, nama_barang, harga_per_barang):
        self.nama_barang = nama_barang
        self.harga_per_barang = harga_per_barang
        self.jumlah_beli = 0

    def hitung_total(self):
        return self.jumlah_beli * self.harga_per_barang


# Meminta informasi pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")
alamat_pelanggan = input("Masukkan alamat pelanggan: ")
no_telp_pelanggan = input("Masukkan nomor telepon pelanggan: ")
tanggal_pembelian = input("Masukkan tanggal pembelian: ")

# Membuat daftar barang
barang1 = KasirMaterial("Cat", 50000)
barang2 = KasirMaterial("Semennya", 75000)
barang3 = KasirMaterial("Batu bata", 2000)

# Meminta input untuk setiap barang
for barang in [barang1, barang2, barang3]:
    while True:
        try:
            jumlah_beli = int(input(f"Jumlah {barang.nama_barang} yang ingin dibeli: "))
            if jumlah_beli >= 0:
                barang.jumlah_beli = jumlah_beli
                break
            else:
                print("Masukkan jumlah yang valid (tidak boleh negatif).")
        except ValueError:
            print("Masukkan angka yang valid.")

# Menampilkan rincian pembelian
print("\nRincian Pembelian:")
print(f"Nama Pelanggan: {nama_pelanggan}")
print(f"Alamat: {alamat_pelanggan}")
print(f"No. Telepon: {no_telp_pelanggan}")
print(f"Tanggal Pembelian: {tanggal_pembelian}\n")

total_pembelian = 0
for barang in [barang1, barang2, barang3]:
    total_barang = barang.hitung_total()
    total_pembelian += total_barang
    print(f"{barang.nama_barang} - Harga per Barang: Rp{barang.harga_per_barang:,} x {barang.jumlah_beli} = Rp{total_barang:,}")

print("\nTotal Pembelian: Rp{:,}".format(total_pembelian))

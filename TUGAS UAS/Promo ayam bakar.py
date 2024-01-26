# Memberikan daftar bagian ayam
daftar_bagian = {
    1: "Paha Atas",
    2: "Paha Bawah",
    3: "Dada",
    4: "Sayap"
}

# Inisialisasi harga ayam bakar per potong
harga_ayam_per_potong = 15000

# Memperkenalkan program kepada pengguna
print("Selamat datang di Program Pembelian Ayam Bakar!")

# Menampilkan daftar film yang akan dipilih
print("Daftar Film:")
for id_bagian, bagian_ayam in daftar_bagian.items():
    print(f"{id_bagian}. {bagian_ayam}")

# Meminta input dari pengguna
# Meminta input daftar film dengan no urut firmnya
id_bagian = int(input("Pilih nomor film yang ingin ditonton: "))

# Meminta input pengguna untuk jumlah ayam yang ingin dibeli
while True:
    try:
        jumlah_ayam = int(input("Berapa potong ayam bakar yang ingin Anda beli? "))
        if jumlah_ayam > 0:
            break
        else:
            print("Masukkan jumlah ayam yang valid (minimal 1 potong).")
    except ValueError:
        print("Masukkan angka yang valid.")

# Menghitung total harga tanpa promo
total_harga = jumlah_ayam * harga_ayam_per_potong

# Promo diskon untuk pembelian lebih dari 5 potong
if jumlah_ayam > 5:
    diskon = 0.1  # 10% diskon
    potongan_harga = total_harga * diskon
    total_harga_setelah_diskon = total_harga - potongan_harga
    promo = f"Selamat! Anda mendapatkan diskon {diskon * 100}%"
else:
    potongan_harga = 0
    total_harga_setelah_diskon = total_harga
    promo = "Maaf, tidak ada diskon untuk pembelian kurang dari 6 potong."

# Menampilkan rincian pembelian dan total harga
print("\nRincian Pembelian:")
print(f"Bagian ayam : {daftar_bagian[id_bagian]}")
print(f"Jumlah Ayam Bakar: {jumlah_ayam} potong")
print(f"Harga Ayam Bakar per Potong: Rp{harga_ayam_per_potong:,}")
print(f"Total Harga (tanpa diskon): Rp{total_harga:,}")
print(promo)
print(f"Total Harga (setelah diskon): Rp{total_harga_setelah_diskon:,.2f}")

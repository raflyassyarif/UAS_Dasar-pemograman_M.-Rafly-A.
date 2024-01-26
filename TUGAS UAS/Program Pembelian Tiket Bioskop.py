# Program Pembelian Tiket Bioskop

# Memberikan Daftar film yang tersedia
daftar_film = {
    1: "Ancika",
    2: "Pengabdi Setan",
    3: "Boboiboy Galaxy Movie",
    4: "One Piece Movie Red"
}

# Harga tiket
# Menentukan harga tiket biasa
harga_biasa = 45000
# Menentukan harga tiket VIP
harga_vip = 60000
# Menentukan harga tiket 3D
harga_3D = 75000
# Memperkenalkan program kepada pengguna
print("Selamat datang di Program Pembelian Tiket Bioskop!")

# Menampilkan daftar film yang akan dipilih
print("Daftar Film:")
for id_film, judul_film in daftar_film.items():
    print(f"{id_film}. {judul_film}")

# Meminta input dari pengguna
# Meminta input daftar film dengan no urut firmnya
id_film = int(input("Pilih nomor film yang ingin ditonton: "))
# Meminta input jumlah tiket yang diinginkan
jumlah_tiket = int(input("Jumlah tiket yang ingin dibeli: "))
# Meminta input jenis tiket yang diinginkan (biasa,VIP,3D)
jenis_tiket = input("Jenis tiket (Biasa/VIP/3D): ")
# Menghitung total biaya yang akan dibayarkan berdasarkan jumlah dan jenis tiketnya
# Menghitung total biaya untuk tiket biasa
if jenis_tiket.lower() == "biasa":
    total_biaya = jumlah_tiket * harga_biasa
# Menghitung total biaya untuk tiket VIP   
elif jenis_tiket.lower() == "vip":
    total_biaya = jumlah_tiket * harga_vip
# Menghitung total biaya untuk tiket 3D    
elif jenis_tiket.lower() == "3d":
    total_biaya = jumlah_tiket * harga_3D
# Bentuk output jika tidak memilih salah satu jenis tiket yang tersedia 
else:
    print("Jenis tiket tidak valid. Silakan pilih antara Biasa, VIP atau 3D.")
    exit()

# Menampilkan ringkasan pembelian
print("\nRingkasan Pembelian:")
# Menampilkan judul film yang dipilih
print(f"Film yang dipilih: {daftar_film[id_film]}")
# Menampilkan jumlah tiket yang diinginkan
print(f"Jumlah tiket: {jumlah_tiket}")
# Menampilkan jenis tiket yang dipilih
print(f"Jenis tiket: {jenis_tiket}")
# Menampilkan total biasa yang harus dibayarkan
print(f"Total biaya: Rp {total_biaya}")

# Terima kasih kepada pengguna
print("\nTerima kasih telah menggunakan program ini. Selamat menonton!")
# Program Kasir Kereta Api

# Harga tiket
# Harga tiket pelajar
harga_pelajar = 100000
# Harga 1 tiket eksekutif
harga_eksekutif = 250000
# Harga 1 tiket ekonomi
harga_ekonomi = 190000
# Harga 1 tiket VIP 
harga_vip = 300000
# Harga 1 tiket VVIP
harga_vvip = 400000

# Memperkenalkan program kepada pengguna
print("Selamat datang di Program Kasir Kereta Api!")

# Meminta input dari pengguna
# Meminta input nama dari pembeli
nama = input("Masukkan Nama Anda: ")
# Meminta untuk menginput tempat tujuan akhir
tujuan = input("Masukkan tujuan perjalanan: ")
# Meminta untuk menginput kelas (eksekutif/ekonomi)
kelas = input("Pilih kelas tiket (Pelajar/Eksekutif/Ekonomi/VIP/VVIP): ")
# Meminta untuk menginput jumlah tiket yang di inginkan
jumlah_tiket = int(input("Jumlah tiket yang ingin dibeli: "))

# Menghitung total biaya
# Menghitung untuk biaya tiket pelajar
if kelas.lower() == "pelajar":
    total_biaya = jumlah_tiket * harga_pelajar
# Menghitung untuk biaya tiket eksekutif    
elif kelas.lower() == "eksekutif":
    total_biaya = jumlah_tiket * harga_eksekutif
# Menghitung untuk biaya ekonomi    
elif kelas.lower() == "ekonomi":
    total_biaya = jumlah_tiket * harga_ekonomi
# Menghitung untuk biasa VIP
elif kelas.lower() == "vip":
    total_biaya = jumlah_tiket * harga_vip
# Menghitung untuk biasa VVIP    
elif kelas.lower() == "vvip":
    total_biaya = jumlah_tiket * harga_vvip        
# Menghitung untuk selain ekonomi dan eksekutif    
else:
    print("Kelas tiket tidak valid. Silakan pilih antara Eksekutif atau Ekonomi.")
    exit()

# Menampilkan ringkasan pembelian
print("\nRingkasan Pembelian")
print("\nBerikut adalah data pembelian tiket anda")
# Menampilkan Nama pelanggan
print(f"Nama: {nama}")
# Menampilkan Tujuan pertajalan yang di tuju
print(f"Tujuan perjalanan: {tujuan}")
# Menampilkan kelas tiket yang di pilih
print(f"Kelas tiket: {kelas}")
# Menampilkan jumlah tiket yang di inginkan
print(f"Jumlah tiket: {jumlah_tiket}")
# Menampilkan total biaya yang harus dibayarkan
print(f"Total biaya: Rp {total_biaya}")

# Mengucap kan Terima kasih kepada pengguna
print("\nTerima kasih telah menggunakan program ini. Selamat berperjalanan!")

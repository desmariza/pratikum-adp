#desmariza_2410432035

# Memasukkan data pribadi
print("===struk pemesanan tiket pesawat===")
print("assalamualaikum wr.wb")
nama = input("Masukkan nama pelanggan: ")
umur = int(input("Masukkan umur pelanggan: "))
jenis_kelamin = input("Masukkan jenis kelamin pelanggan(male/female): ")


# Memasukkan kode maskapai dan memilih tujuan
print("\nPilih kode maskapai:")
print("3012 - Padang-Jakarta")
print("4015 - Padang-Batam")
print("4050 - Padang-Bandung")
kode_maskapai = input("Masukkan kode maskapai: ")

# Menentukan kelas yang akan di pilih oleh pelanggan
if kode_maskapai == "3012":
    tujuan = "Padang-Jakarta"
    harga_kelas_ekonomi = 800000
    harga_kelas_bisnis = 850000
    harga_kelas_first_class = 900000
elif kode_maskapai == "4015":
    tujuan = "Padang-Batam"
    harga_kelas_ekonomi = 500000
    harga_kelas_bisnis = 550000
    harga_kelas_first_class = 700000
elif kode_maskapai == "4050":
    tujuan = "Padang-Bandung"
    harga_kelas_ekonomi = 700000
    harga_kelas_bisnis = 750000
    harga_kelas_first_class = 850000
else:
    print("Kode maskapai tidak ada.")
    exit()

# Memilih kelas dan jumlah tiket
print("\nPilih kelas maskapai:")
print("1 - Ekonomi (Rp.{})".format(harga_kelas_ekonomi))
print("2 - Bisnis (Rp.{})".format(harga_kelas_bisnis))
print("3 - First Class (Rp.{})".format(harga_kelas_first_class))
pilihan_kelas = int(input("Masukkan pilihan kelas (1/2/3): "))
jumlah_tiket = int(input("Masukkan jumlah tiket yang dipesan: "))

# Menghitung harga total
if pilihan_kelas == 1:
    jenis_kelas = "Ekonomi"
    harga_total = harga_kelas_ekonomi * jumlah_tiket
elif pilihan_kelas == 2:
    jenis_kelas = "Bisnis"
    harga_total = harga_kelas_bisnis * jumlah_tiket
elif pilihan_kelas == 3:
    jenis_kelas = "First Class"
    harga_total = harga_kelas_first_class * jumlah_tiket
else:
    print("Pilihan kelas tidak ada.")
    exit()

# terapkan diskon jika membeli lebih dari 3 tiket
if jumlah_tiket >=3:
    harga_total *= 0.8

# Menampilkan struk pemesanan
print("-----------------------------------")
print("=== Struk Pemesanan tiket pesawat ===:")
print("------------------------------------")
print("Nama pelanggan: ", nama)
print("Umur pelanngan: ", umur)
print("Jenis Kelamin pelanggan: ", jenis_kelamin)
print("Kode Maskapai: ", kode_maskapai)
print("Tujuan Maskapai: ", tujuan)
print("Jenis kelas Maskapai: ", jenis_kelas)
print("Jumlah tiket: ", jumlah_tiket)
print("total harga: rp.{:,}".format(int(harga_total)))
print("===================================")

print("TUGAS MODUL 8")
print("NAMA = DESMARIZA")
print("NIM = 2410432035")
print("=============================================")
print("DAFTAR INVENTARIS TOKO BUKU MINI PUSTAKA KITA")
print("=============================================")

def buat_data_awal():
    data_buku = {
        "9786020321997": {"Judul": "Bumi", "Penulis": "Tere Liye", "Stok": 15, "Harga Beli": 65000, "Harga Jual": 98000},
        "9786020322000": {"Judul": "Bulan", "Penulis": "Tere Liye", "Stok": 1, "Harga Beli": 68000, "Harga Jual": 102000},
        "9789793062792": {"Judul": "Laskar Pelangi", "Penulis": "Andrea Hirata", "Stok": 25, "Harga Beli": 75000, "Harga Jual": 112000},
        "9786020325285": {"Judul": "Sang Pemimpi", "Penulis": "Andrea Hirata", "Stok": 18, "Harga Beli": 70000, "Harga Jual": 105000},
        "9786020325292": {"Judul": "Cantik Itu Luka", "Penulis": "Eka Kurniawan", "Stok": 10, "Harga Beli": 85000, "Harga Jual": 128000},
        "9786020325308": {"Judul": "Lelaki Harimau", "Penulis": "Eka Kurniawan", "Stok": 8, "Harga Beli": 78000, "Harga Jual": 117000},
        "9786020325315": {"Judul": "Serangkaian Cerita tentang Cinta", "Penulis": "Ika Natasya", "Stok": 7, "Harga Beli": 60000, "Harga Jual": 90000},
        "9786020325322": {"Judul": "Antologi Rasa", "Penulis": "Ika Natasya", "Stok": 3, "Harga Beli": 55000, "Harga Jual": 82500},
        "9786020325339": {"Judul": "Perahu Kertas", "Penulis": "Dee Lestari", "Stok": 14, "Harga Beli": 72000, "Harga Jual": 108000},
        "9786020325346": {"Judul": "Supernova", "Penulis": "Dee Lestari", "Stok": 9, "Harga Beli": 80000, "Harga Jual": 120000},
        "9786020325353": {"Judul": "Negeri 5 Menara", "Penulis": "Ahmad Fuadi", "Stok": 20, "Harga Beli": 68000, "Harga Jual": 102000},
        "9786020325360": {"Judul": "Rantau 1 Muara", "Penulis": "Ahmad Fuadi", "Stok": 2, "Harga Beli": 72000, "Harga Jual": 108000},
        "9786020325377": {"Judul": "Ayat-Ayat Cinta", "Penulis": "Habiburrahman El Shirazy", "Stok": 22, "Harga Beli": 75000, "Harga Jual": 112500},
        "9786020325384": {"Judul": "Ketika Cinta Bertasbih", "Penulis": "Habiburrahman El Shirazy", "Stok": 18, "Harga Beli": 78000, "Harga Jual": 117000},
        "9786020325391": {"Judul": "Pulang", "Penulis": "Leila S. Chudori", "Stok": 11, "Harga Beli": 82000, "Harga Jual": 123000}
    }
    with open("inventaris_buku.txt", "w") as file:
        for isbn, buku in data_buku.items():
            file.write(f"{isbn},{buku['Judul']},{buku['Penulis']},{buku['Stok']},{buku['Harga Beli']},{buku['Harga Jual']}\n")

def baca_data():
    inventaris = {}
    with open("inventaris_buku.txt", "r") as file:
        for baris in file:
            bagian = []
            bagian_sekarang = ""
            for karakter in baris:
                if karakter == ',':
                    bagian.append(bagian_sekarang)
                    bagian_sekarang = ""
                else:
                        bagian_sekarang += karakter
            bagian.append(bagian_sekarang)

            if len(bagian) == 6:
                isbn = bagian[0]
                inventaris[isbn] = {
                    "Judul": bagian[1],
                    "Penulis": bagian[2],
                    "Stok": int(bagian[3]),
                    "Harga Beli": int(bagian[4]),
                    "Harga Jual": int(bagian[5]),
                }
    return inventaris

def buat_laporan(inventaris):
    with open("laporan_inventaris.txt", "w") as file:
        file.write("ISBN,Judul Buku,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
        for isbn, buku in inventaris.items():
            keuntungan = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
            file.write(f"{isbn},{buku['Judul']},{buku['Penulis']},{buku['Stok']},{buku['Harga Beli']},{buku['Harga Jual']},{keuntungan}\n")

def analisis_inventaris(inventaris):
    jumlah_buku = len(inventaris)
    if jumlah_buku == 0:
        print("Inventaris kosong, tidak ada data untuk dianalisis.")
        return

    def hitung_keuntungan(buku):
        return (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
    
    items = list(inventaris.items())
    buku_pertama = items[0]
    buku_keuntungan_tertinggi = buku_pertama
    buku_keuntungan_terendah = buku_pertama
    keuntungan_tertinggi = hitung_keuntungan(buku_pertama[1])
    keuntungan_terendah = keuntungan_tertinggi
    
    for i in range(1, jumlah_buku):
        isbn, buku = items[i]
        keuntungan = hitung_keuntungan(buku)
        
        if keuntungan > keuntungan_tertinggi:
            keuntungan_tertinggi = keuntungan
            buku_keuntungan_tertinggi = (isbn, buku)
            
        if keuntungan < keuntungan_terendah:
            keuntungan_terendah = keuntungan
            buku_keuntungan_terendah = (isbn, buku)
    
    total_nilai_inventaris = 0
    for buku in inventaris.values():
        total_nilai_inventaris += buku["Stok"] * buku["Harga Beli"]
    
    stok_menipis = []
    for isbn, buku in inventaris.items():
        if buku["Stok"] < 5:
            stok_menipis.append(isbn)

    print("\n ANALISIS INVENTARIS TOKO BUKU MINI PUSTAKA KITA")
    print("=" * 60)
    print(f" Potensi Keuntungan Tertinggi: {buku_keuntungan_tertinggi[1]['Judul']} (ISBN: {buku_keuntungan_tertinggi[0]}, Rp {(buku_keuntungan_tertinggi[1]['Harga Jual'] - buku_keuntungan_tertinggi[1]['Harga Beli']) * buku_keuntungan_tertinggi[1]['Stok']:,})")
    print(f" Potensi Keuntungan Terendah: {buku_keuntungan_terendah[1]['Judul']} (ISBN: {buku_keuntungan_terendah[0]}, Rp {(buku_keuntungan_terendah[1]['Harga Jual'] - buku_keuntungan_terendah[1]['Harga Beli']) * buku_keuntungan_terendah[1]['Stok']:,})")
    print(f" Total Nilai Inventaris: Rp {total_nilai_inventaris:,}")

    print("\n Buku yang perlu di-restock (stok < 5):")
    if stok_menipis:
        for isbn in stok_menipis:
            print(f" - {inventaris[isbn]['Judul']} (ISBN: {isbn}, Stok: {inventaris[isbn]['Stok']})")
    else:
        print(" Tidak ada buku yang perlu di-restock saat ini.")
    print("=" * 60)

print(" Membuat data awal toko buku mini pustaka kita")
buat_data_awal()
print(" Membaca data inventaris toko buku mini pustaka kita")
inventaris = baca_data()
print(" Membuat laporan inventaris toko buku mini pustaka kita")
buat_laporan(inventaris)
print(" Melakukan analisis inventaris toko buku mini pustaka kita")
analisis_inventaris(inventaris)
print("\n Selesai! File laporan disimpan sebagai 'laporan_inventaris.txt'")
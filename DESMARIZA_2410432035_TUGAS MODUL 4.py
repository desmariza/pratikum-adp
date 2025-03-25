
print("------------------------------------------------------")
print("selamat datang di bioskop,silahkan pesan kursi bioskop")
print("------------------------------------------------------")

r = int(input("Masukkan jumlah baris yang akan dipesan(minimal 4): "))
c = int(input("Masukkan jumlah kolom yang akan dipesan (minimal 4): "))
if r<4 or c<4 :
    print("baris dan kolom minimal 4x4,coba lagi!")
    r=int(input("masukkan baris yang akan pesan (minimal 4) :"))
    c=int(input("masukkan kolom yang akan pesan (minimal 4) :"))

kursi_terpesan = ""
rc = r * c

while True:
    
    print("\n====DAFTAR KURSI TERSEDIA====")
    no_kursi = 1
    for i in range(r):
        for j in range(c):
            if f",{no_kursi}," in kursi_terpesan:
                print("X", end="\t")
            else:
                print(no_kursi, end="\t")
            no_kursi += 1
        print()

    pilih = int(input("\nMasukkan nomor kursi yang ingin dipesan (atau 0 untuk selesai): "))
    if pilih == 0:
        print("Terima kasih telah memesan tiket!")
        break

    if pilih < 1 or pilih > rc:
        print(f"Kursi {pilih} tidak tersedia! Pilih nomor antara 1 - {rc}.")
        continue

    if f",{pilih}," in kursi_terpesan:
        print("Kursi sudah dipesan! Pilih kursi lain.")
        continue

    print(f"Kursi {pilih} berhasil dipesan!")
    kursi_terpesan += f",{pilih},"

print("-----------------------------------")
print("semoga menikmati film nya,happy fun!")        
print("-----------------------------------")
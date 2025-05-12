print("TUGAS MODUL 5")
print("NAMA = DESMARIZA")
print("NIM = 2410432035")
print("======================================")
print("NILAI AKHIR MAHASISWA  PRATIKUM ADP")
print("======================================")
jumlah_siswa = int(input("Masukkan jumlah siswa: "))
data_siswa = []
total_nilai = 0

for i in range(jumlah_siswa):
    print(f"\nData siswa ke-{i+1}")
    nama = input("Nama siswa  : ")
    pretest = float(input("Nilai pretest: "))
    posttest = float(input("Nilai posttest: "))
    paper = float(input("Nilai paper   : "))

    nilai_akhir = (pretest * 0.4) + (posttest * 0.4) + (paper * 0.2)
    total_nilai += nilai_akhir
    
    data_siswa.append([nama, nilai_akhir])

rata_rata = total_nilai / jumlah_siswa

print("\n" + "=" * 40)
print(f"{'No.':<4} | {'Nama Mahasiswa':<20} | {'Nilai Akhir':>12}")
print("=" * 40)

for i in range(len(data_siswa)):
    nama, nilai = data_siswa[i]
    print(f"{i+1:<4} | {nama:<20} | {nilai:>12.1f}")

print("\ndaftar mahasiswa di aatas rata-rata kelas:")
print("-" * 30)
for i in range(len(data_siswa)):
    nama, nilai = data_siswa[i]
    status = "di atas rata-rata kelas" if nilai > rata_rata else "di bawah rata-rata kelas"
    print(f"{i+1}. {nama:<20} : {status}")

tertinggi = data_siswa[0]
terendah = data_siswa[0]
for siswa in data_siswa:
    if siswa[1] > tertinggi[1]:
        tertinggi = siswa
    if siswa[1] < terendah[1]:
        terendah = siswa

print("\n" + "=" * 40)
print(f"Rata-rata kelas: {rata_rata:.1f}")
print(f"Nilai tertinggi: {tertinggi[0]} ({tertinggi[1]:.1f})")
print(f"Nilai terendah : {terendah[0]} ({terendah[1]:.1f})")
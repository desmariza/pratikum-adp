print("TUGAS MODUL 7")
print("NAMA = DESMARIZA")
print("NIM = 2410432035")
print("======================================")
print("TABEL NILAI MAHASISWA")
print("======================================")


def input_data():
    data = []
    n = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(n):
        print(f"\nData ke-{i+1}:")
        nama = input("Nama      : ")
        nim = input("NIM       : ")
        uts = float(input("Nilai UTS : "))
        uas = float(input("Nilai UAS : "))
        tugas = float(input("Nilai Tugas: "))
        nilai_akhir = 0.35*uas + 0.35*uts + 0.3*tugas 
        data.append((nama, nim, uts, uas, tugas, nilai_akhir))
    return data

def urutkan_data(data):
    data_diurutkan = []
    while data:
        tertinggi = data[0]
        for nama in data:
            if nama[5] > tertinggi[5]:
                tertinggi = nama
        data_diurutkan.append(tertinggi)
        data.remove(tertinggi)
    return data_diurutkan

def hitung_rata(data, n):
    rata_uts = sum(nama[2] for nama in data)/n 
    rata_uas = sum(nama[3] for nama in data)/n 
    rata_tugas = sum(nama[4] for nama in data)/n 
    rata_akhir = sum(nama[5] for nama in data)/n 
    return rata_uts, rata_uas, rata_tugas, rata_akhir

def tampilkan_hasil(data, rata_uts, rata_uas, rata_tugas, rata_akhir):
    print("\n+----+-----------------+---------------+------+------+-------+-------+---------+")
    print("| No   | Nama            | NIM           | UTS  | UAS  | Tugas | Akhir | Peringkat|")
    print("+------+-----------------+---------------+------+------+-------+-------+---------+")
    
    i = 1
    for nama in data:
        print(f"| {i:<4} | {nama[0]:<15} | {nama[1]:<12}  | {nama[2]:<4.1f} | {nama[3]:<4.1f} | {nama[4]:<5.1f} | {nama[5]:<5.1f} | {i:<7} |")
        i += 1
    
    print("+------+-----------------+---------------+------+------+-------+-------+---------+")
    print(f"| Rata |{'':^12}     |{'':^12}   | {rata_uts:.1f} | {rata_uas:.1f} | {rata_tugas:.1f}  | {rata_akhir:.1f}  |         |")
    print("+------+-----------------+---------------+------+------+-------+-------+---------+")

data = input_data()
data_diurutkan = urutkan_data(data.copy())
rata_uts, rata_uas, rata_tugas, rata_akhir = hitung_rata(data_diurutkan, len(data_diurutkan))
tampilkan_hasil(data_diurutkan, rata_uts, rata_uas, rata_tugas, rata_akhir)

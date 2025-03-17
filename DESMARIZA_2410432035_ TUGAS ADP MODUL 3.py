print("TUGAS MODUL 3")
print("NAMA = DESMARIZA")
print("NIM = 2410432035")
print("======================================")
print("SELAMAT DATANG DI GAME TEBAK ANGKA BOM")
print("======================================")

print("pemain 1")
x=int(input("pilih angka dari 1 sampai yang kamu mau :"))
z=int(input("masukkan angka bom :"))

for x in range(1,x):
    if x % z == 0: 
        print(x,"BOM")
    else:
        print(x,"BUKAN BOM")
print("pemain 2")

while True:
    dugaan_angka = int(input(f"Pemain 2, duga angka dari 1 - {x+1}: "))

    if 1 <= dugaan_angka >= x+1 :
        print(f"Angka tebakan harus berada dalam rentang 1 - {x+1}, silakan masukkan angka baru.")
        continue

    elif dugaan_angka %z==0 :
        print(dugaan_angka,"dugaan anda benar,selamat")
        break
    else:
        print(dugaan_angka,"dugaan  anda salah,semangat coba lagi!")

print("---------------------------------------------------")
print("TERIMA KASIH TELAH MEMAINKAN GAME TEBAK ANGKA BOM")
print("---------------------------------------------------")





    
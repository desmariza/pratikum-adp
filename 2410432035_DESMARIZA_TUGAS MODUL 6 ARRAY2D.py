print("TUGAS MODUL 6")
print("NAMA = DESMARIZA")
print("NIM = 2410432035")
print("======================================")
print("KALKULATOR MATRIKS MANUAL")
print("======================================")

n = int(input("Masukkan jumlah baris matriks A: "))
m = int(input("Masukkan jumlah kolom matriks A: "))
print("Masukkan elemen matriks A:")
A = []
for i in range(n):
    baris = []
    for j in range(m):
        elemmen = float(input(f"Baris {i+1}, Kolom {j+1}: "))
        baris.append(elemmen)
    A.append(baris)

p = int(input("Masukkan jumlah baris matriks B: "))
q = int(input("Masukkan jumlah kolom matriks B: "))
print("Masukkan elemen matriks B:")
B = []
for i in range(p):
    baris = []
    for j in range(q):
        elemmen = float(input(f"Baris {i+1}, Kolom {j+1}: "))
        baris.append(elemmen)
    B.append(baris)

while True:
    print("\nMenu Operasi:")
    print("1. Penjumlahan (A+B)")
    print("2. Pengurangan (A-B)")
    print("3. Perkalian (A×B)")
    print("4. Determinan (A dan B)")
    print("5. Invers (A dan B)")
    print("6. Transpose (A dan B)")
    print("0. Keluar")
    pilihan = input("Pilih operasi (0-6): ")

    if pilihan == "0":
        print("Program selesai.")
        break

    # Penjumlahan
    elif pilihan == "1":
        if n != p or m != q:
            print("Error: Ukuran matriks tidak sama!")
        else:
            hasil = []
            for i in range(n):
                baris = []
                for j in range(m):
                    baris.append(A[i][j] + B[i][j])
                hasil.append(baris)
            print("\nA + B:")
            for baris in hasil:
                for x in baris:
                    print(f"{x:6.2f}", end="  ")
                print()
    
    # Pengurangan
    elif pilihan == "2":
        if n != p or m != q:
            print("Error: Ukuran matriks tidak sama!")
        else:
            hasil = []
            for i in range(n):
                baris = []
                for j in range(m):
                    baris.append(A[i][j] - B[i][j])
                hasil.append(baris)
            print("\nA - B:")
            for baris in hasil:
                for x in baris:
                    print(f"{x:6.2f}", end="  ")
                print()

    # Perkalian
    elif pilihan == "3":
        if m != p:
            print("Error: Kolom A ≠ Baris B!")
        else:
            hasil = []
            for i in range(n):
                baris = []
                for j in range(q):
                    total = 0
                    for k in range(m):
                        total += A[i][k] * B[k][j]
                    baris.append(total)
                hasil.append(baris)
            print("\nA × B:")
            for baris in hasil:
                for x in baris:
                    print(f"{x:6.2f}", end="  ")
                print()

    # Determinan
    elif pilihan == "4":
        # Determinan A
        if n != m:
            print("\nA bukan matriks persegi!")
        else:
            if n == 2:
                det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                print(f"\nDeterminan A: {det_A:.2f}")
            elif n == 3:
                a, b, c = A[0]
                d, e, f = A[1]
                g, h, i = A[2]
                det_A = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
                print(f"\nDeterminan A: {det_A:.2f}")
            else:
                print("\nHanya support matriks 2x2 dan 3x3")

        # Determinan B
        if p != q:
            print("B bukan matriks persegi!")
        else:
            if p == 2:
                det_B = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                print(f"Determinan B: {det_B:.2f}")
            elif p == 3:
                a, b, c = B[0]
                d, e, f = B[1]
                g, h, i = B[2]
                det_B = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
                print(f"Determinan B: {det_B:.2f}")
            else:
                print("Hanya support matriks 2x2 dan 3x3")

    # Invers
    elif pilihan == "5":
        # Invers A
        if n != m:
            print("\nA bukan matriks persegi!")
        else:
            if n == 2:
                det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                if det_A == 0:
                    print("\nA tidak memiliki invers (determinan = 0)")
                else:
                    invers_a = [
                        [A[1][1]/det_A, -A[0][1]/det_A],
                        [-A[1][0]/det_A, A[0][0]/det_A]
                    ]
                    print("\nInvers A:")
                    for baris in invers_a:
                        for x in baris:
                            print(f"{x:6.2f}", end="  ")
                        print()
            elif n == 3:
                a, b, c = A[0]
                d, e, f = A[1]
                g, h, i = A[2]
                det_A = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
                if det_A == 0:
                    print("\nA tidak memiliki invers (determinan = 0)")
                else:
                    kofaktors = []
                    for i_baris in range(3):
                        kofaktor_baris = []
                        for j_kolom in range(3):
                            minor = []
                            for x in range(3):
                                if x == i_baris:
                                    continue
                                minor_x = []
                                for y in range(3):
                                    if y == j_kolom:
                                        continue
                                    minor_x.append(A[x][y])
                                minor.append(minor_x)
                            minor_det = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
                            tanda = (-1) ** (i_baris + j_kolom)
                            kofaktor = tanda * minor_det
                            kofaktor_baris.append(kofaktor)
                        kofaktors.append(kofaktor_baris)
                    tranpose_kofaktor = []
                    for j in range(3):
                        adj_baris = []
                        for i in range(3):
                            adj_baris.append(kofaktors[i][j])
                        tranpose_kofaktor.append(adj_baris)
                    invers_A = []
                    for baris in tranpose_kofaktor:
                        invers_baris = [elem / det_A for elem in baris]
                        invers_A.append(invers_baris)
                    print("\nInvers A:")
                    for baris in invers_A:
                        for x in baris:
                            print(f"{x:6.2f}", end="  ")
                        print()
            else:
                print("\nInvers hanya tersedia untuk 2x2 dan 3x3")

        # Invers B
        if p != q:
            print("B bukan matriks persegi!")
        else:
            if p == 2:
                det_B = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                if det_B == 0:
                    print("B tidak memiliki invers (determinan = 0)")
                else:
                    invers_b = [
                        [B[1][1]/det_B, -B[0][1]/det_B],
                        [-B[1][0]/det_B, B[0][0]/det_B]
                    ]
                    print("\nInvers B:")
                    for baris in invers_b:
                        for x in baris:
                            print(f"{x:6.2f}", end="  ")
                        print()
            elif p == 3:
                a, b, c = B[0]
                d, e, f = B[1]
                g, h, i = B[2]
                det_B = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
                if det_B == 0:
                    print("B tidak memiliki invers (determinan = 0)")
                else:
                    kofaktors = []
                    for i_baris in range(3):
                        kofaktor_baris = []
                        for j_kolom in range(3):
                            minor = []
                            for x in range(3):
                                if x == i_baris:
                                    continue
                                minor_x = []
                                for y in range(3):
                                    if y == j_kolom:
                                        continue
                                    minor_x.append(B[x][y])
                                minor.append(minor_x)
                            minor_det = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
                            tanda = (-1) ** (i_baris + j_kolom)
                            kofaktor = tanda * minor_det
                            kofaktor_baris.append(kofaktor)
                        kofaktors.append(kofaktor_baris)
                    tranpose_kofaktor = []
                    for j in range(3):
                        adj_baris = []
                        for i in range(3):
                            adj_baris.append(kofaktors[i][j])
                        tranpose_kofaktor.append(adj_baris)
                    invers_B = []
                    for baris in tranpose_kofaktor:
                        invers_baris = [elem / det_B for elem in baris]
                        invers_B.append(invers_baris)
                    print("\nInvers B:")
                    for baris in invers_B:
                        for x in baris:
                            print(f"{x:6.2f}", end="  ")
                        print()
            else:
                print("Invers hanya tersedia untuk 2x2 dan 3x3")

    # Transpos
    elif pilihan == "6":
        # Transpos A
        transpos_A = []
        for j in range(m):
            baris = []
            for i in range(n):
                baris.append(A[i][j])
            transpos_A.append(baris)
        print("\nTranspose A:")
        for baris in transpos_A:
            for x in baris:
                print(f"{x:6.2f}", end="  ")
            print()

        # Transpose B
        transpos_B = []
        for j in range(q):
            baris = []
            for i in range(p):
                baris.append(B[i][j])
            transpos_B.append(baris)
        print("\nTranspose B:")
        for baris in transpos_B:
            for x in baris:
                print(f"{x:6.2f}", end="  ")
            print()

    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk pilihan menu lain....")
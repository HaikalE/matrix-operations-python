def menu_lanjut(pilihan):
    if pilihan<1 or pilihan>4:
        print("Bukan pilihan yang benar")
        return
    print(f"Baik anda memilih menu-{pilihan}")
    print("Silahkan masukkan matriks A")
    arr1=penginputan_matriks()
    print("Silahkan masukkan matriks B")
    arr2=penginputan_matriks()
    if(cek_persyaratan(arr1,arr2,pilihan)==False):
        print(f"Anda tidak memenuhi persyaratan matriks untuk operasi pada menu-{pilihan}")
    if pilihan==1:
        hasil=penjumlahan_matriks(arr1,arr2)
        print("HASIL PENJUMLAHAN MATRIKS!: ")
        for i in hasil:
            for j in i:
                print(f"{j:2d}",end=" ")
            print()
    elif pilihan==2:
        hasil=pengurangan_matriks(arr1,arr2)
        print("HASIL PENGURANGAN MATRIKS!: ")
        for i in hasil:
            for j in i:
                print(f"{j:2d}",end=" ")
            print()
    elif pilihan==3:
        hasil=perkalian_matriks(arr1,arr2)
        print("HASIL PERKALIAN YAITU : ")
        for i in hasil:
            for j in i:
                print(f"{j:2d}",end=" ")
            print()
    elif pilihan==4 :
        if(pengecekan_matriks_satuan(arr1)==True):
            print("Matriks A adalah matriks satuan")
        else :
            print("Matriks A bukan matriks satuan")
        if(pengecekan_matriks_satuan(arr2)==True):
            print("Matriks B adalah matriks satuan")
        else :
            print("Matriks B bukan matriks satuan")

def perkalian_matriks(arr1,arr2):
    baris_A,kolom_A=len(arr1),len(arr1[0])
    kolom_B=len(arr2[0])
    hasil = [[0 for j in range(kolom_B)] for i in range(baris_A)]
    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A): 
                hasil[i][j] += arr1[i][k] * arr2[k][j]
    return hasil

def pengecekan_matriks_satuan(arr):
    baris = len(arr)
    kolom = len(arr[0])
    for i in range(baris):
        for j in range(kolom):
            if arr[i][j] not in [0, 1]:
                return False
    return True

def cek_persyaratan(arr1,arr2,pilihan):
    if pilihan==3:
        if len(arr1)==len(arr1[0]) and len(arr2)==len(arr2[0]):
            return True
    elif pilihan==1 or pilihan==2:
        print("Pengecekan operasi penjumlahan atau pengurangan")
        if len(arr1)==len(arr2) and len(arr1[0])==len(arr2[0]):
            return True
    else :
        if len(arr1[0])==len(arr2):
            return True
    return False

def penginputan_matriks():
    baris=3 
    kolom=3
    arr = [[0 for j in range(kolom)] for i in range(baris)]
    for i in range(baris):
        for j in range(kolom):
            arr[i][j]=int(input(f"Masukkan array pada baris ke-{i+1} dan kolom ke-{j+1}: "))
    return arr

def penjumlahan_matriks(arr1,arr2):
    baris_A,kolom_A=len(arr1),len(arr1[0])
    C = [[0 for j in range(kolom_A)] for i in range(baris_A)]
    for i in range(baris_A):
        for j in range(kolom_A):
            C[i][j] = arr1[i][j] + arr2[i][j]
    return C

def pengurangan_matriks(arr1,arr2):
    baris_A,kolom_A=len(arr1),len(arr1[0])
    C = [[0 for j in range(kolom_A)] for i in range(baris_A)]
    for i in range(baris_A):
        for j in range(kolom_A):
            C[i][j] = arr1[i][j] - arr2[i][j]
    return C

def menu_awal():
    print("Silahkan pilih menu: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Cek matriks satuan")
    pilihan=int(input("Silahkan pilih menu diatas!: "))
    menu_lanjut(pilihan)

if __name__=="__main__":
    menu_awal()
    

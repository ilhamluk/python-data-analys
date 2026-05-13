a = 10
b = 5
plus = a + b 
minus = a - b
multiple =  a * b
divide = a / b
print (plus)
print (minus)
print (divide)

#bagi bulat
c=10
d= 3
bagi_bulat = 10 // 3
print(f"bagi bulat dari {c} dengan {d} ialah {bagi_bulat}")
#bagi sisa (modulo)
bagi_sisa = 10 % 3
print(f"bagi SISA dari {c} dengan {d} ialah {bagi_sisa}")
#pangkat
pangkat = c ** d
print(f"pangkat dari {c} dengan {d} ialah {pangkat}")
a = 100
b = 10**2
c = 101

a_apakah_sama_dengan_b = a == b
a_apakah_sama_dengan_c = a == c
print(f"nilai a adalah {a}")
print(f"nilai b adalah {b}")
print(f"nilai c adalah {c}")
print(f"a apakah sama dengan b? {a_apakah_sama_dengan_b}")
print(f"a apakah sama dengan c? {a_apakah_sama_dengan_c}")

a_apakah_tdk_sama_dengan_c = a != c
print(f"a apakah tidak sama dengan c? {a_apakah_tdk_sama_dengan_c}")

a_lebih_besar_dari_b = a > b
print(f"a lebih besar dari b? {a_lebih_besar_dari_b}")
a_lebih_kecil_dari_c = a < c
print(f"{a} lebih kecil dari {c}? {a_lebih_kecil_dari_c}")

a_lebih_kecil_sama_dengan_c = a <= c
print(f"{a} lebih kecil sama dengan {c}? {a_lebih_kecil_sama_dengan_c}")

nilai = int(input("Masukkan Nilai: "))
if nilai >= 80:
    print ("A")
elif nilai >= 70:
    print ("B")
elif nilai >= 50:
    print ("C")
else :
    print ("D")
def add(a, b):
    total = a + b
    return total

print(add(10, 5))

jumlah = add(10, 5)
print(f"Jumlah dari 10 dan 5 = {jumlah}")
#pengurangan
def add(a,b):
    total = a-b
    return total
print(add(10,5))
jumlah = add(10,5)

def bmi(berat = None, tinggi = None):
    if berat == None or tinggi == None:
        print ("parameter tidak lengkap")
        return
    total =berat/((tinggi/100)**2)
    return total
def bmi_check (bmi):
    if bmi <18.5:
        print("Kategori : berat badan kurang")
    elif bmi  < 25:
        print("Kategori : berat badan normal")
    elif  bmi < 30:
        print("Kategori : berat badan berlebih")
    else:
      print("kategori : obesitas")
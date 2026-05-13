#program menghitung BMI
berat = float(input("Masukan berat badan (kg): "))
tinggi = float(input("Masukan tinggi badan (cm): "))
#Menggitung BMI
bmi = berat/((tinggi/100) ** 2 )
print ("BMI anda adalah :", bmi)
#menentukan kategori bmi
if bmi <18.5:
    print("Kategori : berat badan kurang")
elif bmi  < 25:
    print("Kategori : berat badan normal")
elif  bmi < 30:
    print("Kategori : berat badan berlebih")
else:
    print("kategori : obesitas")
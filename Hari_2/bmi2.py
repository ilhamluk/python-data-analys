#program menghitung BMI
berat = float(input("Masukan berat badan (kg): "))
tinggi = float(input("Masukan tinggi badan (cm): "))
#Menggitung BMI
def hitung_bmi (berat, tinggi):
    return berat/((tinggi/100) ** 2 )

#menentukan kategori bmi
def kategori_bmi (bmi):
    if bmi <18.5:
        return "Kategori : berat badan kurang"
    elif bmi  < 25:
        return "Kategori : berat badan normal"
    elif  bmi < 30:
        return "Kategori : berat badan berlebih"
    else:
        return "kategori : obesitas"

    

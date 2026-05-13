import Aritmatika as i

berat = float(input("Masukan berat badan (kg): "))
tinggi = float(input("Masukan tinggi badan (cm): "))

bmi= i.bmi(berat,tinggi)
print("BMI Kamu adalah", bmi)
i.bmi_check(bmi)

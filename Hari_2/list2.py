index = [0, 1, 2, 3, 4,5,6]
nama = ["Alice", "Bob", "Farah", "Edi", "Charlie", "Gita", "Hasti"]
nama_slice_3_tengah = nama[2:5]

print(nama_slice_3_tengah)

nama_slice_3_tengah[2] = "Clara"
print("/n")
print(nama_slice_3_tengah)

#insert
nama_slice_3_tengah.insert(1, "Zara")
print("/n INSERT")
print(nama_slice_3_tengah)
#Append
nama_slice_3_tengah.append("Dina")
print("/n APPEND")
print(nama_slice_3_tengah)
#sort
nama_slice_3_tengah.sort()
print("/n SORT")
print(nama_slice_3_tengah)
#POP
nama_slice_3_tengah.pop()
print("/n POP")
print(nama_slice_3_tengah)
#REVERSE
nama_slice_3_tengah.reverse()
print("/n REVERSE")
print(nama_slice_3_tengah)

#menampilkan informasi program

print("Konversi Suhu (Reamur ke Kelvin")

#input suhu dalam Reamur
R = float(input("Masukkan nilai suhu (Reamur): "))

#menghitung suhu dari Reamur ke Kelvin
K = 273.15 + (R * (5 / 4))

#menampilkan suhu Kelvin
print("Kelvin: ", K)
import math

#fungsi lambda untuk menghitung lngkaran
luas_lingkaran = lambda r: math.pi * r**2 #menghitung luas lingkaran


#input dari pengguna
jari_jari = float(input("Masukkan jari-jari Lingkaran: "))

#menghitung dan mencetak hasil luas lingkaran
hasil_luas =luas_lingkaran(jari_jari)
print(f"Luas Lingkaran dengan jari-jari {jari_jari} adalah: {hasil_luas:.2f}")

def konversi_suhu(temp, unit):
    if unit.upper() == 'C':
        return (temp * 9/5) + 32 # celcius to fahrenheit
    elif unit.upper() == 'f':
        return (temp - 32) * 5/9 #farenheit to celcius
    else:
        raise ValueError("Unit Tidak Valid. Gunakan 'C' atau 'F'.")
    
#input dari pengguna
temp = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan unit suhu ('C' untuk Celcius, 'F' untuk Fahrenheit):")

#menghitung dan mencetak hasil luas lingkaran
hasil = konversi_suhu(temp,unit)
if hasil is not None:
    print(f"Hasil konversi: {hasil:2f} {'F' if unit.upper() ==  'C' else 'C'}")
else:
    print("unit tidak valid. Gunakan 'C' atau 'F'.")


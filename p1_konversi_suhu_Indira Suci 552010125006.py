

def konversi_suhu(celcius):
    fahrenheit = (9/5 * celcius) + 32
    kelvin = celcius + 273.15
    return fahrenheit, kelvin


# Program utama
celcius = float(input("Masukkan suhu dalam Celcius: "))

fahrenheit, kelvin = konversi_suhu(celcius)

print("\n=== HASIL KONVERSI ===")
print("Celcius     :", celcius)
print("Fahrenheit  :", fahrenheit)
print("Kelvin      :", kelvin)
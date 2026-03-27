# Nama: Indira Suci Fitriani
# Program Studi: Teknik Informatika
# NIM: 552010125006
# Semester 2
# praktikum latihan 1 - implementasi kasus diskon

def hitung_total_bayar(total_belanja):
    if total_belanja >= 500000:
        diskon = 0.2 * total_belanja
    elif total_belanja >= 250000:
        diskon = 0.1 * total_belanja
    else:
        diskon = 0
    
    total_bayar = total_belanja - diskon
    return diskon, total_bayar


# Program utama
total_belanja = float(input("Masukkan total belanja: "))

diskon, total_bayar = hitung_total_bayar(total_belanja)

print("\n=== RINCIAN PEMBAYARAN ===")
print("Total Belanja : Rp", total_belanja)
print("Diskon        : Rp", diskon)
print("Total Bayar   : Rp", total_bayar)
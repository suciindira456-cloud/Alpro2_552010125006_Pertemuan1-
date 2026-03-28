# Nama: Indira Suci Fitriani
# Program Studi: Teknik Informatika
# NIM: 552010125006
# Praktikum latihan 2 - nilai akhir

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

def validasi_nilai(nilai):
    return 0 <= nilai <= 100


# Program utama
tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

if validasi_nilai(tugas) and validasi_nilai(uts) and validasi_nilai(uas):
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    
    print("\n=== HASIL PERHITUNGAN ===")
    print("Nilai akhir:", nilai_akhir)
else:
    print("Input tidak valid! Nilai harus 0–100.")

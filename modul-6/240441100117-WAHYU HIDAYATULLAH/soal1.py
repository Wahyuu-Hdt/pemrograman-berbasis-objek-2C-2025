class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi
    
class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        pi = 22 / 7
        return pi * self.jari_jari * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun):
    print(f"Luas {type(bangun).__name__}: {bangun.luas():.2f}")

while True:
    print("=== Hitung Luas Bangun Datar ===")

    sisi = float(input("Masukkan panjang sisi persegi: "))
    persegi = Persegi(sisi)

    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    lingkaran = Lingkaran(jari_jari)

    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    segitiga = Segitiga(alas, tinggi)

    print("\n=== Hasil Luas Bangun Datar ===")
    for bangun in [persegi, lingkaran, segitiga]:
        cetak_luas(bangun)
    
    n = input("Apakah ingin memasukan nilai lagi? (y/n) ")
    if n != "y":
        break
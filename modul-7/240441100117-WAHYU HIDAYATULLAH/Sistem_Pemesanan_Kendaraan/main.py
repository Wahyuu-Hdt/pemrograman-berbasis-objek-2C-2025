from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main ():
    while True:
        print("Selamat Datang di Jasa Sewa Kendaraan")
        print("Jenis Kendaraan:")
        print("1. Mobil")
        print("2. Motor")
        print("3. Sepeda")

        pilihan = int(input("Silahkan pilih jenis kendaraan: "))

        if pilihan == 1:
            nama = input("Masukkan nama anda: ")
            usia = int(input("Masukkan usia anda: "))
            kendaraan = Mobil()
        elif pilihan == 2:
            nama = input("Masukkan nama anda: ")
            usia = int(input("Masukkan usia anda: "))
            kendaraan = Motor()
        elif pilihan == 3:
            nama = input("Masukkan nama anda: ")
            usia = int(input("Masukkan usia anda: "))
            kendaraan = Sepeda()
        else:
            print("pilihan tidak valid!")
            exit()
        
        if kendaraan.p_booking(nama, usia):
            biaya = kendaraan.h_biaya()
            asuransi = kendaraan.asuransi()
            print(f"Total Biaya: Rp{biaya} + Asuransi: Rp{asuransi} = Rp{biaya+asuransi}")
        
        n = input("Ingin menyewa kendaraan lain (y/n): ")
        if n != "y":
            break
main()
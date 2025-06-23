from tunai import Tunai
from kartu import KartuKredit
from dompet import DompetDigital

def main():
    while True:
        print("Pilih Metode Pembayaran")
        print("1. Tunai")
        print("2. Kartu Kredit")
        print("3. Dompet Digital")

        pilihan = int(input("Silahkan Pilih Metode Pembayaran: "))

        if pilihan == 1:
            jumlah = float(input("Masukkan jumlah pembayaran: Rp "))
            metode = Tunai(jumlah)
        elif pilihan == 2:
            jumlah = float(input("Masukkan jumlah pembayaran: Rp "))
            metode = KartuKredit(jumlah)
        elif pilihan == 3:
            jumlah = float(input("Masukkan jumlah pembayaran: Rp "))
            metode = DompetDigital(jumlah)
        else:
            print("Pilihan tidak valid!")
            exit()
        
        metode.p_pembayaran()
        
        n = input("Mau setor lagi (y/n): ")
        if n != "y":
            break

main()
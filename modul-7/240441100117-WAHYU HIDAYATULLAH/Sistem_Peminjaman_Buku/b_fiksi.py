from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def pinjam(self, nama):
        print(f"{nama} meminjam buku fiksi.")

    def reservasi(self, nama):
        print(f"{nama} melakukan reservasi buku fiksi.")
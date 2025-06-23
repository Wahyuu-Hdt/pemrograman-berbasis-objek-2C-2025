from peminjaman import Peminjaman
from reservasi import Reservasi

class BukuReferensi(Peminjaman, Reservasi):
    def pinjam(self, nama):
        print(f"{nama} buku hanya bisa dibaca di tempat")

    def reservasi(self, nama):
        print(f"{nama} melakukan reservasi buku referensi.")
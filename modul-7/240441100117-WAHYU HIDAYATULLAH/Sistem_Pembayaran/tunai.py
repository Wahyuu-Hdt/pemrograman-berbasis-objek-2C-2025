from m_pembayaran import Pembayaran
class Tunai(Pembayaran):
    def p_pembayaran(self):
        potongan = 0.05 * self.jumlah
        total = self.jumlah - potongan
        print(f"Bayar Tunai. Diskon: Rp {potongan}. Total Bayar: Rp {total}")
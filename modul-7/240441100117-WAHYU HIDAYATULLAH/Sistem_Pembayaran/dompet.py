from m_pembayaran import Pembayaran
class DompetDigital(Pembayaran):
    def p_pembayaran(self):
        potongan = 0.02 * self.jumlah
        total = self.jumlah - potongan
        print(f"Bayar Dompet Digital. Diskon: Rp {potongan}. Total Bayar: Rp {total}")
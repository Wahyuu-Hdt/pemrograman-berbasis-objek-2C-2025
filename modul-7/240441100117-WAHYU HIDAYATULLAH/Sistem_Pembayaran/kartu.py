from m_pembayaran import Pembayaran
class KartuKredit(Pembayaran):
    def p_pembayaran(self):
        b_admin = 0.03 * self.jumlah
        total = self.jumlah + b_admin
        print(f"Bayar Kartu Kredit. Biaya Admin: Rp {b_admin}. Total Bayar: Rp {total}")
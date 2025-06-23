from kendaraan import Kendaraan

class Sepeda(Kendaraan):
    def p_booking(self, nama):
        print(f"Booking Sepeda untuk {nama} berhasil.")
        return True

    def h_biaya(self):
        return 50000

    def asuransi(self):
        return 10000
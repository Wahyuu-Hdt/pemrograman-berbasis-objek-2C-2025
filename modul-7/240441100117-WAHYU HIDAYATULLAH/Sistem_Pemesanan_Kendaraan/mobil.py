from kendaraan import Kendaraan

class Mobil(Kendaraan):
    def p_booking(self, nama, usia):
        if usia < 21:
            print("Usia minimal untuk sewa mobil adalah 21 tahun.")
            return False
        print(f"Booking Mobil untuk mas {nama} berhasil.")
        return True

    def h_biaya(self):
        return 500000

    def asuransi(self):
        return 100000
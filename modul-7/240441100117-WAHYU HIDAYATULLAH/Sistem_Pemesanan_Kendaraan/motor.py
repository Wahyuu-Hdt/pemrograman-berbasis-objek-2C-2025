from kendaraan import Kendaraan

class Motor(Kendaraan):
    def p_booking(self, nama, usia):
        if usia < 17:
            print("Usia minimal untuk sewa motor adalah 17 tahun.")
            return False
        print(f"Booking Motor untuk mas {nama} berhasil.")
        return True

    def h_biaya(self):
        return 100000

    def asuransi(self):
        return 30000
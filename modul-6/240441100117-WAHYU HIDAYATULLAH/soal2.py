from abc import ABC, abstractmethod
class Karyawan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama)
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

class KaryawanKontrak(Karyawan):
    def __init__(self, nama, jam_kerja, upah_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.upah_per_jam

def cetak_gaji(karyawan: Karyawan):
    if isinstance(karyawan, KaryawanTetap):
        jenis = "Karyawan Tetap"
    elif isinstance(karyawan, KaryawanKontrak):
        jenis = "Karyawan Kontrak"
    else:
        jenis = "Karyawan Tidak Dikenal"

    print(f"{jenis} - {karyawan.nama}")
    print(f"Gaji: Rp{karyawan.hitung_gaji()}")

while True:
    print("=== Input Data Karyawan ===")
    jenis = input("Jenis karyawan (tetap/kontrak): ")

    if jenis == "tetap":
        nama = input("Nama: ")
        gaji_pokok = int(input("Gaji pokok: "))
        tunjangan = int(input("Tunjangan: "))
        karyawan = KaryawanTetap(nama, gaji_pokok, tunjangan)
    elif jenis == "kontrak":
        nama = input("Nama: ")
        jam_kerja = int(input("Jumlah jam kerja: "))
        upah_per_jam = int(input("Upah per jam: "))
        karyawan = KaryawanKontrak(nama, jam_kerja, upah_per_jam)
    else:
        print("Jenis karyawan tidak valid.")
        exit()

    cetak_gaji(karyawan)
    n = input("Apakah mau inputkan lagi? (y/n)")
    if n != "y":
        break
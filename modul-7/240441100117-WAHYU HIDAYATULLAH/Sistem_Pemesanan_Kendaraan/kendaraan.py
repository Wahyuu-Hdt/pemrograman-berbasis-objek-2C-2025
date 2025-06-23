from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def p_booking(self, nama, usia):
        pass

    @abstractmethod
    def h_biaya(self):
        pass

    @abstractmethod
    def asuransi(self):
        pass
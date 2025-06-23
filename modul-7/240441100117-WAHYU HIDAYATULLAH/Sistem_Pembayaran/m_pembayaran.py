from abc import ABC, abstractmethod

class Pembayaran(ABC):
    def __init__(self, jumlah):
        self.__jumlah = jumlah

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, value):
        self.__jumlah = value

    @abstractmethod
    def p_pembayaran(self):
        pass
from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, nama, harga):
        self._nama = nama
        self.__harga = harga

    @abstractmethod
    def tampilkan_info(self):
        pass

    @property
    def nama(self):
        return self._nama

    @property
    def harga(self):
        return self.__harga

# models/makanan.py

class Makanan:
    def __init__(self, nama, harga, tipe, gambar):
        self.nama = nama
        self.harga = harga
        self.tipe = tipe
        self.gambar = gambar  # ✅ penting

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

    def get_tipe(self):
        return self.tipe

    def get_gambar(self):
        return self.gambar  # ✅ method ini juga bisa dipakai di template jika kamu ingin

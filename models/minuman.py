from .menu_item import MenuItem

class Minuman(MenuItem):
    def tampilkan_info(self):
        print(f"[Minuman] {self.get_nama()} - Rp{self.get_harga()}")

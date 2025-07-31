from .menu_item import MenuItem

class Makanan(MenuItem):
    def tampilkan_info(self):
        print(f"[Makanan] {self.get_nama()} - Rp{self.get_harga()}")

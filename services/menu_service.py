import json
from models.makanan import Makanan
from models.minuman import Minuman

def load_menu(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    daftar_menu = []
    for item in data:
        if item['tipe'] == 'Makanan':
            menu = Makanan(item['nama'], item['harga'])
        elif item['tipe'] == 'Minuman':
            menu = Minuman(item['nama'], item['harga'])
        daftar_menu.append(menu)
    return daftar_menu

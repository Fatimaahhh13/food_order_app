import json
from models.makanan import Makanan

def load_menu():
    with open('data/menu.json', 'r') as file:
        data = json.load(file)
        return [Makanan(d['nama'], d['harga'], d['tipe'], d['gambar']) for d in data]

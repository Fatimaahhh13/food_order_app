import json
import os

def simpan_pesanan(file_path, pesanan):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = []

    data.append(pesanan)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

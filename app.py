from flask import Flask, render_template, request
from utils.menu_loader import load_menu
from models.pesanan import Pesanan

app = Flask(__name__)

@app.route('/')
def index():
    menu = load_menu()
    return render_template('index.html', menu=menu)

@app.route('/pesan', methods=['POST'])
def pesan():
    menu_data = request.form['menu_data']
    jumlah = int(request.form['jumlah'])
    nama, harga = menu_data.split('|')
    pesanan = Pesanan(nama, int(harga), jumlah)
    return render_template('succes.html', pesanan=pesanan)

if __name__ == '__main__':
    app.run(debug=True)

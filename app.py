from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Menu lengkap dengan kategori
menu = [
    {
        "nama": "Burger Keju",
        "harga": 25000,
        "gambar": "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Burger Daging Double",
        "harga": 35000,
        "gambar": "https://cdn.pixabay.com/photo/2016/03/05/19/02/hamburger-1238246_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Kentang Goreng",
        "harga": 15000,
        "gambar": "https://cdn.pixabay.com/photo/2016/03/05/20/07/french-fries-1238246_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Nugget Ayam",
        "harga": 18000,
        "gambar": "https://cdn.pixabay.com/photo/2023/07/17/10/48/fried-chicken-8132426_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Pizza Pepperoni",
        "harga": 45000,
        "gambar": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Pizza Keju",
        "harga": 42000,
        "gambar": "https://cdn.pixabay.com/photo/2020/02/23/17/06/pizza-4874094_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Hotdog Jumbo",
        "harga": 20000,
        "gambar": "https://cdn.pixabay.com/photo/2016/03/05/19/02/hot-dog-1238676_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Taco Sapi",
        "harga": 23000,
        "gambar": "https://cdn.pixabay.com/photo/2021/01/26/14/21/taco-5950919_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Onion Rings",
        "harga": 12000,
        "gambar": "https://cdn.pixabay.com/photo/2022/07/06/13/59/onion-rings-7304842_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Fried Chicken",
        "harga": 27000,
        "gambar": "https://cdn.pixabay.com/photo/2021/06/10/09/50/fried-chicken-6325143_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Es Krim Coklat",
        "harga": 10000,
        "gambar": "https://cdn.pixabay.com/photo/2017/03/27/13/28/ice-cream-2178882_1280.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Es Krim Vanila",
        "harga": 10000,
        "gambar": "https://cdn.pixabay.com/photo/2014/07/31/23/10/ice-cream-407098_1280.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Milkshake Coklat",
        "harga": 14000,
        "gambar": "https://cdn.pixabay.com/photo/2016/03/05/19/02/milkshake-1238247_1280.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Soft Drink",
        "harga": 8000,
        "gambar": "https://cdn.pixabay.com/photo/2015/01/06/19/28/cola-591751_1280.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Es Teh Manis",
        "harga": 7000,
        "gambar": "https://cdn.pixabay.com/photo/2020/06/22/20/09/iced-tea-5329602_1280.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Kopi Dingin",
        "harga": 12000,
        "gambar": "https://cdn.pixabay.com/photo/2016/11/29/04/00/coffee-1869769_1280.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Cheese Fries",
        "harga": 17000,
        "gambar": "https://cdn.pixabay.com/photo/2017/05/07/08/56/cheese-fries-2297523_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Spaghetti Bolognese",
        "harga": 32000,
        "gambar": "https://cdn.pixabay.com/photo/2017/07/16/10/43/spaghetti-2500373_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Lasagna Daging",
        "harga": 36000,
        "gambar": "https://cdn.pixabay.com/photo/2017/03/27/13/27/lasagna-2178860_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Mozzarella Sticks",
        "harga": 16000,
        "gambar": "https://cdn.pixabay.com/photo/2017/07/16/10/44/mozzarella-sticks-2500376_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Chicken Wrap",
        "harga": 24000,
        "gambar": "https://cdn.pixabay.com/photo/2016/06/30/00/42/wrap-1484062_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Donat Gula",
        "harga": 9000,
        "gambar": "https://cdn.pixabay.com/photo/2017/07/16/10/44/doughnut-2500378_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Salad Sayur Segar",
        "harga": 15000,
        "gambar": "https://cdn.pixabay.com/photo/2017/08/07/01/09/salad-2591863_1280.jpg",
        "kategori": "Makanan"
    }
]

# Data pesanan akan disimpan sementara dalam list
pesanan_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def halaman_menu():
    return render_template('menu.html', menu=menu)

@app.route('/riwayat_pesanan')
def halaman_pemesanan():
    return render_template('riwayat_pesanan.html', pesanan=pesanan_list)

@app.route('/api/menu')
def api_menu():
    return jsonify(menu)

@app.route('/api/pesan', methods=['POST'])
def api_pesan():
    data = request.json
    if 'pesanan' in data:
        pesanan_list.extend(data['pesanan'])
        return jsonify({"message": "Pesanan berhasil diterima!"})
    else:
        return jsonify({"message": "Tidak ada pesanan yang dikirim."}), 400

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify, request
# flask (framework)
# render_template (menampilkan html untuk API)
# jsonify (mengubah data python ke format json)
# request (mengakses permintaan pengguna)

app = Flask(__name__)
# objek utama flask

# Menu lengkap dengan kategori
menu = [
    {
        "nama": "Burger Keju",
        "harga": 25000,
        "gambar": "https://i.pinimg.com/1200x/9b/eb/fd/9bebfdf8e3c0e0133e0613c3df423345.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Burger Daging Double",
        "harga": 35000,
        "gambar": "https://i.pinimg.com/736x/20/d0/d7/20d0d725a913d16d2486d26affac2fc4.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Kentang Goreng",
        "harga": 15000,
        "gambar": "https://i.pinimg.com/736x/51/30/2e/51302ec5fbd95944281940debf39e79b.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Nugget Ayam",
        "harga": 18000,
        "gambar": "https://i.pinimg.com/1200x/44/84/9b/44849b125f605e8f0c6b3fcd4e0d7f5b.jpg",
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
        "gambar": "https://cdn.pixabay.com/photo/2017/12/05/20/09/pizza-3000274_1280.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Hotdog Jumbo",
        "harga": 20000,
        "gambar": "https://i.pinimg.com/736x/c4/c4/db/c4c4dbb9d0f9bab138fa48b96661c90f.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Taco Sapi",
        "harga": 23000,
        "gambar": "https://i.pinimg.com/1200x/d3/62/6c/d3626c5af61c7750708f116bd44f8024.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Onion Rings",
        "harga": 12000,
        "gambar": "https://i.pinimg.com/1200x/01/3b/3f/013b3f776c0f6e2e8d1cf55bb08098bf.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Fried Chicken",
        "harga": 27000,
        "gambar": "https://i.pinimg.com/736x/54/31/2a/54312aefcb222d75fe69e1be747ad48c.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Es Krim Coklat",
        "harga": 10000,
        "gambar": "https://i.pinimg.com/736x/54/c4/41/54c441f4a4f097e96d628611ef8c1ce4.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Es Krim Vanila",
        "harga": 10000,
        "gambar": "https://i.pinimg.com/1200x/58/65/14/586514553069b7f4a38003db9b93bd7c.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Milkshake Coklat",
        "harga": 14000,
        "gambar": "https://i.pinimg.com/1200x/d9/30/5e/d9305edce30213c10c944c6fb386d40b.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Milkshake Strawberry",
        "harga": 8000,
        "gambar": "https://i.pinimg.com/736x/32/92/44/3292440cae636b3f0b294ceceadde04e.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Es Teh Manis",
        "harga": 7000,
        "gambar": "https://i.pinimg.com/736x/b6/6d/74/b66d741de51766e948601c924e278db8.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Cappucino Assino",
        "harga": 12000,
        "gambar": "https://i.pinimg.com/736x/f8/56/1e/f8561ea80e14bd1989b4fe87736e1468.jpg",
        "kategori": "Minuman"
    },
    {
        "nama": "Cheese Fries",
        "harga": 17000,
        "gambar": "https://i.pinimg.com/1200x/6c/f9/25/6cf92550e20f7f109be4c47ef54ac789.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Spaghetti Bolognese",
        "harga": 32000,
        "gambar": "https://i.pinimg.com/736x/94/ed/51/94ed516e1d1ed82e6a1da3c86ea0877a.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Lasagna Daging",
        "harga": 36000,
        "gambar": "https://i.pinimg.com/1200x/f0/68/c4/f068c457baa25c8c3b3a1b367395a736.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Mozzarella Sticks",
        "harga": 16000,
        "gambar": "https://i.pinimg.com/1200x/20/f4/47/20f447775327c4879f151015d2849611.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Chicken Wrap",
        "harga": 24000,
        "gambar": "https://i.pinimg.com/736x/ac/e9/c0/ace9c035c5fcd2e45f1821319586755a.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Donat Gula",
        "harga": 9000,
        "gambar": "https://i.pinimg.com/736x/77/ab/f3/77abf394d267e8e319be0024acf4c079.jpg",
        "kategori": "Makanan"
    },
    {
        "nama": "Salad Sayur Segar",
        "harga": 15000,
        "gambar": "https://i.pinimg.com/736x/f0/83/ab/f083ab2be8fc38aa9e8c42f72dcd65ff.jpg",
        "kategori": "Makanan"
    }
]

# Data pesanan akan disimpan sementara dalam list
pesanan_list = []

@app.route('/')
def index():
    return render_template('index.html')
# menampilkan halaman index.html

@app.route('/menu')
def halaman_menu():
    return render_template('menu.html', menu=menu)
# menampilkan halaman menu. html dan mengirim data menu ke html agar bisa ditampilkan

@app.route('/riwayat_pesanan')
def halaman_pemesanan():
    total_semua = sum(p['total'] for p in pesanan_list)
    return render_template('riwayat_pesanan.html', pesanan=pesanan_list, total=total_semua)

# Menampilkan halaman berisi semua pesanan yang sudah dikirim pengguna dan menyisipkan pesanan list

@app.route('/api/menu')
def api_menu():
    return jsonify(menu)
# mengirimkan data menu ke format json

@app.route('/api/pesan', methods=['POST'])
def api_pesan():
    data = request.json
    if 'pesanan' in data:
        for item in data['pesanan']:
            nama = item['nama']
            harga = item['harga']
            jumlah = item.get('jumlah', 1)
            total = harga * jumlah
            pesanan_list.append({
                "nama": nama,
                "harga": harga,
                "jumlah": jumlah,
                "total": total
            })
        return jsonify({"message": "Pesanan berhasil masuk ke keranjang!"})
    else:
        return jsonify({"message": "Tidak ada pesanan yang dikirim."}), 400

    # menerima data pesanan

if __name__ == '__main__':
    app.run(debug=True)
# memastikan Flask hanya berjalan saat file ini langsung dieksekusi


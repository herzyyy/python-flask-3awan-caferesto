📌 Deskripsi Proyek

Proyek ini adalah backend API untuk aplikasi Jawan Cafe & Resto, sebuah sistem pemesanan menu restoran yang memungkinkan pelanggan melihat daftar menu, menambah/mengurangi pesanan, dan menghitung total harga.
API ini dibangun menggunakan Python (Flask) dan PostgreSQL serta dihosting menggunakan Railway.

⚙️ Fitur Utama

CRUD Data Menu (Create, Read, Update, Delete)

CRUD Data Transaksi (Pemesanan)

Endpoint publik untuk diakses oleh aplikasi Flutter

Terhubung dengan database PostgreSQL (Railway)

🏗️ Struktur Direktori
3AWAN-CAFERESTO-API/
│
├── config/
│   └── database.py             # Konfigurasi koneksi ke PostgreSQL
│
├── controllers/
│   ├── menu_controller.py      # Logika utama untuk CRUD menu
│   └── transaction_controller.py # Logika utama untuk CRUD transaksi
│
├── models/
│   ├── menu_model.py           # Model ORM tabel menu
│   └── transaction_model.py    # Model ORM tabel transaksi
│
├── routes/
│   └── route.py                # Routing utama API
│
├── viewmodels/
│   ├── menu_viewmodel.py       # Format output data menu ke client
│   └── transaction_viewmodel.py# Format output data transaksi
│
├── views/
│   ├── menu_view.py            # Fungsi endpoint untuk menu
│   └── transaction_view.py     # Fungsi endpoint untuk transaksi
│
├── main.py                     # Entry point Flask app
└── requirements.txt            # Daftar dependensi Python

🧰 Instalasi & Menjalankan Proyek
1️⃣ Clone Repository
git clone https://github.com/username/3awan-caferesto-api.git
cd 3awan-caferesto-api

2️⃣ Buat Virtual Environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Konfigurasi Database

Buat file .env berisi konfigurasi PostgreSQL Railway:

DATABASE_URL=https://python-flask-3awan-caferesto-production.up.railway.app

5️⃣ Jalankan Server Flask
py main.py


Server akan berjalan di:

http://localhost:5000/

🌐 Endpoint API
Method	Endpoint	Deskripsi
GET	/api/menus	Menampilkan semua menu
GET	/api/menus/<id>	Menampilkan menu berdasarkan ID
POST	/api/menus	Menambahkan menu baru
PUT	/api/menus/<id>	Mengupdate menu
DELETE	/api/menus/<id>	Menghapus menu
GET	/api/transactions	Menampilkan semua transaksi
POST	/api/transactions	Membuat transaksi baru

Contoh JSON Menu:

{
  "id": 1,
  "name": "Nasi Goreng",
  "price": 25000,
  "category": "makanan",
  "image_url": "https://..."
}

🚀 Deploy ke Railway

Push ke GitHub.

Hubungkan repo dengan Railway.

Tambahkan variabel DATABASE_URL.

Deploy otomatis → Railway akan memberi URL seperti:

https://python-flask-3awan-caferesto-production.up.railway.app

🧪 Testing API

Gunakan Postman atau cURL:

https://python-flask-3awan-caferesto-production.up.railway.app/menus
https://python-flask-3awan-caferesto-production.up.railway.app/transactions

🧾 Dokumentasi

API Documentation: Swagger (opsional)

Database: PostgreSQL Railway

Framework: Flask

ORM: SQLAlchemy

from flask import Flask, send_from_directory
from flask_cors import CORS
from config.database import Base, engine
from routes.route import menu_bp, transaction_bp
import os

app = Flask(__name__)

# ✅ Aktifkan CORS agar Flutter bisa akses API dan file gambar
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Daftarkan semua blueprint
app.register_blueprint(menu_bp)
app.register_blueprint(transaction_bp)

# ✅ Endpoint tambahan untuk serve gambar dari folder static/uploads
@app.route('/static/uploads/<path:filename>')
def uploaded_file(filename):
    upload_folder = os.path.join(app.root_path, 'static', 'uploads')
    return send_from_directory(upload_folder, filename)

# ✅ Buat tabel otomatis kalau belum ada
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

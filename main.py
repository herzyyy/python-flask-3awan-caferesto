from flask import Flask
from flask_cors import CORS
from config.database import Base, engine
from routes.route import menu_bp
from routes.route import transaction_bp

app = Flask(__name__)

# ✅ Aktifkan CORS agar Flutter bisa akses API
CORS(app, resources={r"/*": {"origins": "*"}})

# Daftarkan semua blueprint
app.register_blueprint(menu_bp)
app.register_blueprint(transaction_bp)

# Buat tabel otomatis kalau belum ada
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

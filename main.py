from flask import Flask
from config.database import Base, engine
from routes.route import menu_bp
from routes.route import transaction_bp

app = Flask(__name__)

# Daftarkan semua blueprint
app.register_blueprint(menu_bp)
app.register_blueprint(transaction_bp)

# Buat tabel otomatis kalau belum ada
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, jsonify, request
from config.database import get_db
from controllers.menu_controller import MenuController
from sqlalchemy.orm import Session

# Buat blueprint agar bisa diregister ke app.py
menu_bp = Blueprint("menu_bp", __name__, url_prefix="/api/menus")

# GET /api/menus → ambil semua data
@menu_bp.route("/", methods=["GET"])
def get_all_menus():
    db: Session = next(get_db())
    controller = MenuController(db)
    menus = controller.get_all()
    return jsonify(menus), 200


# GET /api/menus/<id> → ambil data berdasarkan id
@menu_bp.route("/<int:menu_id>", methods=["GET"])
def get_menu_by_id(menu_id):
    db: Session = next(get_db())
    controller = MenuController(db)
    menu = controller.get_by_id(menu_id)
    if not menu:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify(menu), 200


# POST /api/menus → tambah data baru
@menu_bp.route("/", methods=["POST"])
def create_menu():
    data = request.get_json()
    required_fields = ["name", "price", "category"]

    # Validasi input
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Field '{field}' is required"}), 400

    db: Session = next(get_db())
    controller = MenuController(db)
    new_menu = controller.create(
        name=data["name"],
        price=data["price"],
        category=data["category"],
        image_url=data.get("image_url")
    )
    return jsonify(new_menu), 201


# PUT /api/menus/<id> → update data
@menu_bp.route("/<int:menu_id>", methods=["PUT"])
def update_menu(menu_id):
    data = request.get_json()
    db: Session = next(get_db())
    controller = MenuController(db)
    updated_menu = controller.update(
        menu_id=menu_id,
        name=data.get("name"),
        price=data.get("price"),
        category=data.get("category"),
        image_url=data.get("image_url")
    )
    if not updated_menu:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify(updated_menu), 200


# DELETE /api/menus/<id> → hapus data
@menu_bp.route("/<int:menu_id>", methods=["DELETE"])
def delete_menu(menu_id):
    db: Session = next(get_db())
    controller = MenuController(db)
    deleted = controller.delete(menu_id)
    if not deleted:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify({"message": "Menu deleted successfully"}), 200

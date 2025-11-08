from flask import Blueprint, jsonify, request
from config.database import get_db
from controllers.menu_controller import MenuController
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Buat blueprint agar bisa diregister ke app.py
menu_bp = Blueprint("menu_bp", __name__, url_prefix="/api/menus")

# GET /api/menus → ambil semua data
@menu_bp.route("/", methods=["GET"])
def get_all_menus():
    db: Session = next(get_db())
    try:
        controller = MenuController(db)
        menus = controller.get_all()
        return jsonify(menus), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()


# GET /api/menus/<id> → ambil data berdasarkan id
@menu_bp.route("/<int:menu_id>", methods=["GET"])
def get_menu_by_id(menu_id):
    db: Session = next(get_db())
    try:
        controller = MenuController(db)
        menu = controller.get_by_id(menu_id)
        if not menu:
            return jsonify({"error": "Menu not found"}), 404
        return jsonify(menu), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()


# POST /api/menus → tambah data baru
@menu_bp.route("/", methods=["POST"])
def create_menu():
    db: Session = next(get_db())
    try:
        data = request.get_json()
        
        # Validasi data tidak None
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        required_fields = ["name", "price", "category"]

        # Validasi input
        for field in required_fields:
            if field not in data or data[field] is None:
                return jsonify({"error": f"Field '{field}' is required"}), 400

        # Validasi tipe data
        try:
            price = float(data["price"])
            if price < 0:
                return jsonify({"error": "Price must be a positive number"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "Price must be a valid number"}), 400

        controller = MenuController(db)
        new_menu = controller.create(
            name=data["name"].strip(),
            price=price,
            category=data["category"].strip(),
            image_url=data.get("image_url", "").strip() if data.get("image_url") else None
        )
        return jsonify(new_menu), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()


# PUT /api/menus/<id> → update data
@menu_bp.route("/<int:menu_id>", methods=["PUT"])
def update_menu(menu_id):
    db: Session = next(get_db())
    try:
        data = request.get_json()
        
        # Validasi data tidak None
        if not data:
            return jsonify({"error": "Request body is required"}), 400

        # Validasi minimal ada satu field yang diupdate
        update_fields = ["name", "price", "category", "image_url"]
        if not any(field in data for field in update_fields):
            return jsonify({"error": "At least one field must be provided for update"}), 400

        # Validasi price jika ada
        price = None
        if "price" in data:
            try:
                price = float(data["price"])
                if price < 0:
                    return jsonify({"error": "Price must be a positive number"}), 400
            except (ValueError, TypeError):
                return jsonify({"error": "Price must be a valid number"}), 400

        controller = MenuController(db)
        updated_menu = controller.update(
            menu_id=menu_id,
            name=data.get("name", "").strip() if data.get("name") else None,
            price=price,
            category=data.get("category", "").strip() if data.get("category") else None,
            image_url=data.get("image_url", "").strip() if data.get("image_url") else None
        )
        if not updated_menu:
            return jsonify({"error": "Menu not found"}), 404
        return jsonify(updated_menu), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()


# DELETE /api/menus/<id> → hapus data
@menu_bp.route("/<int:menu_id>", methods=["DELETE"])
def delete_menu(menu_id):
    db: Session = next(get_db())
    try:
        controller = MenuController(db)
        deleted = controller.delete(menu_id)
        if not deleted:
            return jsonify({"error": "Menu not found"}), 404
        return jsonify({"message": "Menu deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()

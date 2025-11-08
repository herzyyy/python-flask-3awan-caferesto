from flask import Blueprint, jsonify, request
from config.database import get_db
from controllers.transaction_controller import TransactionController
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Buat blueprint untuk transaction
transaction_bp = Blueprint("transaction_bp", __name__, url_prefix="/api/transactions")

@transaction_bp.route("/", methods=["GET"])
def get_all_transactions():
    db: Session = next(get_db())
    try:
        controller = TransactionController(db)
        transactions = controller.get_all()
        return jsonify(transactions), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()

@transaction_bp.route("/<int:transaction_id>", methods=["GET"])
def get_transaction_by_id(transaction_id):
    db: Session = next(get_db())
    try:
        controller = TransactionController(db)
        transaction = controller.get_by_id(transaction_id)
        if not transaction:
            return jsonify({"error": "Transaction not found"}), 404
        return jsonify(transaction), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()

@transaction_bp.route("/", methods=["POST"])
def create_transaction():
    db: Session = next(get_db())
    try:
        data = request.get_json()
        
        # Validasi data tidak None
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        required_fields = ["menu_id", "quantity", "payment_method"]

        # Validasi input
        for field in required_fields:
            if field not in data or data[field] is None:
                return jsonify({"error": f"Field '{field}' is required"}), 400

        # Validasi tipe data
        try:
            menu_id = int(data["menu_id"])
            quantity = int(data["quantity"])
            if menu_id <= 0:
                return jsonify({"error": "menu_id must be a positive integer"}), 400
            if quantity <= 0:
                return jsonify({"error": "quantity must be a positive integer"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "menu_id and quantity must be valid integers"}), 400

        # Validasi payment_method
        payment_method = data["payment_method"].strip() if data.get("payment_method") else ""
        if not payment_method:
            return jsonify({"error": "payment_method cannot be empty"}), 400

        controller = TransactionController(db)
        new_transaction = controller.create(
            menu_id=menu_id,
            quantity=quantity,
            payment_method=payment_method
        )
        
        if not new_transaction:
            return jsonify({"error": "Menu not found"}), 404
        
        return jsonify(new_transaction), 201
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()

@transaction_bp.route("/<int:transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):
    db: Session = next(get_db())
    try:
        data = request.get_json()
        
        # Validasi data tidak None
        if not data:
            return jsonify({"error": "Request body is required"}), 400

        required_fields = ["menu_id", "quantity", "payment_method"]

        # Validasi input
        for field in required_fields:
            if field not in data or data[field] is None:
                return jsonify({"error": f"Field '{field}' is required"}), 400

        # Validasi tipe data
        try:
            menu_id = int(data["menu_id"])
            quantity = int(data["quantity"])
            if menu_id <= 0:
                return jsonify({"error": "menu_id must be a positive integer"}), 400
            if quantity <= 0:
                return jsonify({"error": "quantity must be a positive integer"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "menu_id and quantity must be valid integers"}), 400

        # Validasi payment_method
        payment_method = data["payment_method"].strip() if data.get("payment_method") else ""
        if not payment_method:
            return jsonify({"error": "payment_method cannot be empty"}), 400

        controller = TransactionController(db)
        updated_transaction = controller.update(
            transaction_id=transaction_id,
            menu_id=menu_id,
            quantity=quantity,
            payment_method=payment_method
        )
        if not updated_transaction:
            return jsonify({"error": "Transaction or Menu not found"}), 404
        return jsonify(updated_transaction), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()

@transaction_bp.route("/<int:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    db: Session = next(get_db())
    try:
        controller = TransactionController(db)
        result = controller.delete(transaction_id)
        if not result:
            return jsonify({"error": "Transaction not found"}), 404
        return jsonify(result), 200
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    finally:
        db.close()

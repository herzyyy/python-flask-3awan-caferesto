from flask import jsonify, request
from config.database import get_db
from controllers.transaction_controller import TransactionController
from sqlalchemy.orm import Session

def get_all_transactions():
    db: Session = next(get_db())
    controller = TransactionController(db)
    return jsonify(controller.get_all())

def get_transaction_by_id(transaction_id):
    db: Session = next(get_db())
    controller = TransactionController(db)
    transaction = controller.get_by_id(transaction_id)
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(transaction)

def create_transaction():
    data = request.get_json()
    db: Session = next(get_db())
    controller = TransactionController(db)
    new_transaction = controller.create(
        menu_id=data["menu_id"],
        quantity=data["quantity"],
        payment_method=data["payment_method"]
    )
    return jsonify(new_transaction), 201

def update_transaction(transaction_id):
    data = request.get_json()
    db: Session = next(get_db())
    controller = TransactionController(db)
    updated_transaction = controller.update(
        transaction_id=transaction_id,
        menu_id=data["menu_id"],
        quantity=data["quantity"],
        payment_method=data["payment_method"]
    )
    if not updated_transaction:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(updated_transaction)

def delete_transaction(transaction_id):
    db: Session = next(get_db())
    controller = TransactionController(db)
    result = controller.delete(transaction_id)
    if not result:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(result)

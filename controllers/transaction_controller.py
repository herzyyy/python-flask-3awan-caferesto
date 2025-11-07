from models.transaction_model import Transaction
from models.menu_model import Menu
from viewmodels.transaction_viewmodel import TransactionViewModel
from sqlalchemy.orm import Session

class TransactionController:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        transactions = self.db.query(Transaction).all()
        return [TransactionViewModel.from_model(t).__dict__ for t in transactions]

    def get_by_id(self, transaction_id: int):
        transaction = self.db.query(Transaction).filter(Transaction.id == transaction_id).first()
        return TransactionViewModel.from_model(transaction).__dict__ if transaction else None

    def create(self, menu_id: int, quantity: int, payment_method: str):
        # Cek menu yang terkait
        menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        if not menu:
            return None  # Menu tidak ditemukan

        total_price = menu.price * quantity
        new_transaction = Transaction(
            menu_id=menu_id,
            quantity=quantity,
            total_price=total_price,
            payment_method=payment_method
        )

        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(new_transaction)

        return TransactionViewModel.from_model(new_transaction).__dict__

    def update(self, transaction_id: int, menu_id: int, quantity: int, payment_method: str):
        transaction = self.db.query(Transaction).filter(Transaction.id == transaction_id).first()
        if not transaction:
            return None

        menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        if not menu:
            return None

        transaction.menu_id = menu_id
        transaction.quantity = quantity
        transaction.total_price = menu.price * quantity
        transaction.payment_method = payment_method

        self.db.commit()
        self.db.refresh(transaction)
        return TransactionViewModel.from_model(transaction).__dict__

    def delete(self, transaction_id: int):
        transaction = self.db.query(Transaction).filter(Transaction.id == transaction_id).first()
        if not transaction:
            return None
        self.db.delete(transaction)
        self.db.commit()
        return {"message": "Transaction deleted successfully"}

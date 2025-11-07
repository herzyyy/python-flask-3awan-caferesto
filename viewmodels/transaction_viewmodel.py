class TransactionViewModel:
    def __init__(self, id, menu_id, quantity, total_price, payment_method, created_at):
        self.id = id
        self.menu_id = menu_id
        self.quantity = quantity
        self.total_price = float(total_price)
        self.payment_method = payment_method
        self.created_at = created_at

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id,
            menu_id=model.menu_id,
            quantity=model.quantity,
            total_price=model.total_price,
            payment_method=model.payment_method,
            created_at=model.created_at
        )

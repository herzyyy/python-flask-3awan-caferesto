from flask import Blueprint
from views.menu_view import (
    get_all_menus,
    get_menu_by_id,
    create_menu,
    update_menu,
    delete_menu
)
from flask import Blueprint
from views.transaction_view import (
    get_all_transactions,
    get_transaction_by_id,
    create_transaction,
    update_transaction,
    delete_transaction
)

menu_bp = Blueprint("menu", __name__)

# Daftar route
menu_bp.route("/menus", methods=["GET"])(get_all_menus)
menu_bp.route("/menus/<int:menu_id>", methods=["GET"])(get_menu_by_id)
menu_bp.route("/menus", methods=["POST"])(create_menu)
menu_bp.route("/menus/<int:menu_id>", methods=["PUT"])(update_menu)
menu_bp.route("/menus/<int:menu_id>", methods=["DELETE"])(delete_menu)



transaction_bp = Blueprint("transaction", __name__)

# Daftar route
transaction_bp.route("/transactions", methods=["GET"])(get_all_transactions)
transaction_bp.route("/transactions/<int:transaction_id>", methods=["GET"])(get_transaction_by_id)
transaction_bp.route("/transactions", methods=["POST"])(create_transaction)
transaction_bp.route("/transactions/<int:transaction_id>", methods=["PUT"])(update_transaction)
transaction_bp.route("/transactions/<int:transaction_id>", methods=["DELETE"])(delete_transaction)
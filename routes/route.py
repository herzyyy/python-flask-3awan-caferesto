# Import blueprint dari views, bukan fungsi individual
from views.menu_view import menu_bp
from views.transaction_view import transaction_bp

# Blueprint sudah didefinisikan di views, jadi kita hanya perlu export
__all__ = ['menu_bp', 'transaction_bp']
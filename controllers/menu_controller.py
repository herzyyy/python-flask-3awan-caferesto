from models.menu_model import Menu
from viewmodels.menu_viewmodel import MenuViewModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class MenuController:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        try:
            menus = self.db.query(Menu).all()
            return [MenuViewModel.from_model(m).__dict__ for m in menus]
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def get_by_id(self, menu_id: int):
        try:
            menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
            return MenuViewModel.from_model(menu).__dict__ if menu else None
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def create(self, name: str, price: float, category: str, image_url: str = None):
        try:
            new_menu = Menu(name=name, price=price, category=category, image_url=image_url)
            self.db.add(new_menu)
            self.db.commit()
            self.db.refresh(new_menu)
            return MenuViewModel.from_model(new_menu).__dict__
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def update(self, menu_id: int, name: str = None, price: float = None, category: str = None, image_url: str = None):
        try:
            menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
            if not menu:
                return None
            
            # Hanya update field yang tidak None
            if name is not None:
                menu.name = name
            if price is not None:
                menu.price = price
            if category is not None:
                menu.category = category
            if image_url is not None:
                menu.image_url = image_url
            
            self.db.commit()
            self.db.refresh(menu)
            return MenuViewModel.from_model(menu).__dict__
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def delete(self, menu_id: int):
        try:
            menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
            if not menu:
                return None
            self.db.delete(menu)
            self.db.commit()
            return {"message": "Menu deleted successfully"}
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

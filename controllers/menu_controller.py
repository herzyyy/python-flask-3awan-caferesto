from models.menu_model import Menu
from viewmodels.menu_viewmodel import MenuViewModel
from sqlalchemy.orm import Session

class MenuController:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        menus = self.db.query(Menu).all()
        return [MenuViewModel.from_model(m).__dict__ for m in menus]

    def get_by_id(self, menu_id: int):
        menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        return MenuViewModel.from_model(menu).__dict__ if menu else None

    def create(self, name: str, price: float, category: str, image_url: str = None):
        new_menu = Menu(name=name, price=price, category=category, image_url=image_url)
        self.db.add(new_menu)
        self.db.commit()
        self.db.refresh(new_menu)
        return MenuViewModel.from_model(new_menu).__dict__

    def update(self, menu_id: int, name: str, price: float, category: str, image_url: str = None):
        menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        if not menu:
            return None
        menu.name = name
        menu.price = price
        menu.category = category
        menu.image_url = image_url
        self.db.commit()
        self.db.refresh(menu)
        return MenuViewModel.from_model(menu).__dict__

    def delete(self, menu_id: int):
        menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        if not menu:
            return None
        self.db.delete(menu)
        self.db.commit()
        return {"message": "Menu deleted successfully"}

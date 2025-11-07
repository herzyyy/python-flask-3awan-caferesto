from sqlalchemy import Column, Integer, String, Numeric
from config.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(50), nullable=False)
    image_url = Column(String(2555))

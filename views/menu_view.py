from flask import jsonify, request
from config.database import get_db
from controllers.menu_controller import MenuController
from sqlalchemy.orm import Session


def get_all_menus():
    db: Session = next(get_db())
    controller = MenuController(db)
    return jsonify(controller.get_all())


def get_menu_by_id(menu_id):
    db: Session = next(get_db())
    controller = MenuController(db)
    menu = controller.get_by_id(menu_id)
    if not menu:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify(menu)


def create_menu():
    data = request.get_json()
    db: Session = next(get_db())
    controller = MenuController(db)
    new_menu = controller.create(
        name=data["name"],
        price=data["price"],
        category=data["category"],
        image_url=data.get("image_url")
    )
    return jsonify(new_menu), 201


def update_menu(menu_id):
    data = request.get_json()
    db: Session = next(get_db())
    controller = MenuController(db)
    updated_menu = controller.update(
        menu_id=menu_id,
        name=data["name"],
        price=data["price"],
        category=data["category"],
        image_url=data.get("image_url")
    )
    if not updated_menu:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify(updated_menu)


def delete_menu(menu_id):
    db: Session = next(get_db())
    controller = MenuController(db)
    result = controller.delete(menu_id)
    if not result:
        return jsonify({"error": "Menu not found"}), 404
    return jsonify(result)

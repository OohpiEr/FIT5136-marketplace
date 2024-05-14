# from app import App as app
from DbHelper import DbHelper as db


class Admin:
    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        db.add_product(name, brand, description, quantity,
                       sub_category_id, og_price, member_price)

    def delete_product(self, product_id):
        db.delete_product(product_id)

    def update_product(self, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None,
                       og_price=None, member_price=None):
        db.update_product(product_id, name, brand, description,
                          quantity, sub_category_id, og_price, member_price)

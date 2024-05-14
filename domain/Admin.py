#from app import App as app
from DbHelper import DbHelper as db


class Admin:
    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        db.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)

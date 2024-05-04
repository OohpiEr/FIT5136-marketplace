from app import App as app

class Admin:
    def add_product(self, name, brand, description, quantity,
                           sub_category_id, og_price, member_price):
        app.db.add_product(name, brand, description, quantity,
                           sub_category_id, og_price, member_price)

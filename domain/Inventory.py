from DbHelper import DbHelper as db


class Inventory:
    def __init__(self):
        self.__products = db.get_all_products()        
        self.__categories, self.__subcategories = db.get_all_categories()        
    
    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        return db.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)

    def delete_product(self, product_id):
        db.delete_product(product_id)

    def update_product(self, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None, og_price=None, member_price=None):
        db.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price, member_price)

        
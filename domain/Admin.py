# from DbHelper import DbHelper as db 
from app import App as app

class Admin:
    def add_product(self, product):
        app.db.add_product(product)
        
# from DbHelper import DbHelper as db

from domain.ShoppingCart import ShoppingCart
import csv

class Customer:
    def __init__(self,inventory):
        self.inventory = inventory
        self.shopping_cart = ShoppingCart()

    def get_all_products(self):
        return self.inventory.products

    def add_to_cart(self, product):
        self.shopping_cart.add_to_cart(product)

    def view_shopping_cart(self):
        self.shopping_cart.view_cart()

    def checkout(self):
        pass



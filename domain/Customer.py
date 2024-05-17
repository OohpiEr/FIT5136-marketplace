from domain.ShoppingCart import ShoppingCart
from domain.User import User


class Customer(User):
    """Customer class"""

    def __init__(self, id, email, password, inventory):
        """Constructor

        :param inventory: Inventory object. Inventory of the application.
        """
        self.shopping_cart = ShoppingCart()
        super().__init__(id, email, password, inventory)

    def get_all_products(self):
        """Gets all products the customer has access to

        :return: list of products objects
        """
        return self.inventory.products

    def add_to_cart(self, product):
        self.shopping_cart.add_to_cart(product)

    def view_shopping_cart(self):
        self.shopping_cart.view_cart()

    def checkout(self):
        pass

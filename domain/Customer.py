from domain.ShoppingCart import ShoppingCart

class Customer:
    """Customer class"""
    def __init__(self,inventory):
        """Constructor

        :param inventory: Inventory object. Inventory of the application.
        """
        self.inventory = inventory
        self.shopping_cart = ShoppingCart()

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

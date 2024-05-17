from domain.User import User


class Admin(User):
    """Admin class."""

    def __init__(self, id, email, password, inventory):
        """Constructor

        :param inventory: Inventory object for the application.
        """
        super().__init__(id, email, password, inventory)

    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        """Adds a product to the inventory

        :param name: product name
        :param brand: product brand
        :param description: product description
        :param quantity: product quantity
        :param sub_category_id: product category id
        :param og_price: product price
        :param member_price: product member price
        :return: product object of the product added
        """
        return self.inventory.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)

    def delete_product(self, product_id):
        """Deletes a product from the inventory.

        :param product_id: product id
        """
        self.inventory.delete_product(product_id)

    def show_product(self):
        print("Available product information is listed below:")
        for product in self.inventory.products:
            print(product)
            print("========================")

    def update_product(self, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None, og_price=None, member_price=None):
        """Updates the product

        :param product_id: product id
        :param name: product name, defaults to None
        :param brand: product brand, defaults to None
        :param description: product description, defaults to None
        :param quantity: product quantity, defaults to None
        :param sub_category_id: product category id, defaults to None
        :param og_price: product price, defaults to None
        :param member_price: product member price, defaults to None
        """
        self.inventory.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price,
                                      member_price)

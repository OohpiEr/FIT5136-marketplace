class Product:
    """Product class"""

    def __init__(self, product_id, name, brand, description, quantity, sub_category, og_price, member_price):
        """Constructor

        :param product_id: product id, primary key
        :param name: product name
        :param brand: product brand
        :param description: product description
        :param quantity: product quantity
        :param sub_category: product subcategory id
        :param og_price: product price
        :param member_price: product member price
        """
        self.__id = product_id
        self.__name = name
        self.__brand = brand
        self.__description = description
        self.__quantity = quantity
        self.__sub_category = sub_category
        self.__category = sub_category.category
        self.__og_price = og_price
        self.__member_price = member_price

    @property
    def id(self):
        """getter for the id

        :return: product id
        """
        return self.__id

    @property
    def name(self):
        """getter for the name

        :return: product name
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def brand(self):
        """getter for the brand

        :return: product brand
        """
        return self.__brand

    @brand.setter
    def brand(self, value):
        """setter for the brand

        :param value: product brand
        """
        self.__brand = value

    @property
    def description(self):
        """getter for description

        :return: product description
        """
        return self.__description

    @description.setter
    def description(self, value):
        """setter for description

        :param value: product description
        """
        self.__description = value

    @property
    def quantity(self):
        """getter for quantity

        :return: product quantity
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        """setter for quantity

        :param value: product quantity
        """
        self.__quantity = value

    @property
    def sub_category(self):
        """getter for subcategory

        :return: product subcategory
        """
        return self.__sub_category

    @sub_category.setter
    def sub_category(self, value):
        """setter for subcategory

        :param value: product subcategory
        """
        self.__sub_category = value

    @property
    def category(self):
        """getter for the category

        :return: product category
        """
        return self.__category

    @category.setter
    def category(self, value):
        """setter for the category

        :param value: product category
        """
        self.__category = value

    @property
    def og_price(self):
        """getter for the price

        :return: product price
        """
        return self.__og_price

    @og_price.setter
    def og_price(self, value):
        """setter for the price

        :param value: product price
        """
        self.__og_price = value

    @property
    def member_price(self):
        """getter for the member price

        :return: product member price
        """
        return self.__member_price

    @member_price.setter
    def member_price(self, value):
        """setter for the member price

        :param value: member price
        """
        self.__member_price = value

    def __str__(self):
        """To string method

        :return: String representation of product object
        """
        return "    id = {}\n    name = {}\n    brand = {}\n    description = {}\n    quantity = {}\n    category = {}\n    og_price = {}\n    member_price = {}".format(
            self.__id,
            self.__name,
            self.__brand,
            self.__description,
            self.__quantity,
            self.__sub_category.name,
            self.__og_price,
            self.__member_price)

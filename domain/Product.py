class Product:
    def __init__(self, product_id, name, brand, description, quantity, sub_category_id, og_price, member_price):
        self.__id = product_id
        self.__name = name
        self.__brand = brand
        self.__description = description
        self.__quantity = quantity
        self.__sub_category_id = sub_category_id
        self.__og_price = og_price
        self.__member_price = member_price

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def sub_category_id(self):
        return self.__sub_category_id

    @sub_category_id.setter
    def sub_category_id(self, value):
        self.__sub_category_id = value

    @property
    def og_price(self):
        return self.__og_price

    @og_price.setter
    def og_price(self, value):
        self.__og_price = value

    @property
    def member_price(self):
        return self.__member_price

    @member_price.setter
    def member_price(self, value):
        self.__member_price = value

    def __str__(self):
        return "name = {}\nbrand = {}\ndescription = {}\nquantity = {}\ncategory = {}\nog_price = {}\nmember_price = {}".format(
            self.__name,
            self.__brand,
            self.__description,
            self.__quantity,
            self.__sub_category_id,
            self.__og_price,
            self.__member_price)

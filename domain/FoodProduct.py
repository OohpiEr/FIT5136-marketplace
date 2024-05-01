import Product


class FoodProduct(Product):
    def __init__(self, expired_date, ingredients, storage_instructions, allergen_info):
        super().__init__()
        self.__expired_date = expired_date
        self.__ingredients = ingredients
        self.__storage_instructions = storage_instructions
        self.__allergen_info = allergen_info

    @property
    def expired_date(self):
        return self.__expired_date

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def storage_instructions(self):
        return self.__storage_instructions

    @property
    def allergen_info(self):
        return self.__allergen_info

    def __str__(self):
        return f"expired_date = {self.expired_date}\ningredients = {self.ingredients}\nstorage_instructions = {self.storage_instructions}\nallergen_info = {self.allergen_info}"

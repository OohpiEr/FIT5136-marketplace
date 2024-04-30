import Product

class FoodProduct(Product):
    def __init__(self, expired_date, ingredients, storage_instructions, allergen_info):
        self.expired_date = expired_date
        self.ingredients = ingredients
        self.storage_instructions = storage_instructions
        self.allergen_info = allergen_info
    
    def __str__(self):
        return f"expired_date = {self.expired_date}\ningredients = {self.ingredients}\nstorage_instructions = {self.storage_instructions}\nallergen_info = {self.allergen_info}"
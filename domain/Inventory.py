from DbHelper import DbHelper as db


class Inventory:
    def __init__(self):
        self.__categories, self.__subcategories = db.get_all_categories()
        self.__products = db.get_all_products(self.__subcategories)

    @property
    def products(self):
        return self.__products

    @property
    def categories(self):
        return self.__categories

    @property
    def subcategories(self):
        return self.__subcategories
    
    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        product = db.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price, self.__subcategories)
        self.__products.append(product)
        return product

    def delete_product(self, product_id):
        db.delete_product(product_id)
        i, product = self.__get_product(product_id)
        self.__products.pop(i)

    def __get_product(self, product_id):
        for i, product in enumerate(self.__products):
            if product.id == product_id:
                return i, product

    def update_product(self, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None, og_price=None, member_price=None):
        updated_product = db.update_product(product_id, name, brand, description,
                          quantity, sub_category_id, og_price, member_price)

        if updated_product:
            print("Product updated successfully.")
            i, product = self.__get_product(product_id)
            if name != '':
                product.name = name
            if brand != '':
                product.brand = brand
            if description != '':
                product.description = description
            if quantity != '':
                product.quantity = quantity
            if sub_category_id != '':
                product.sub_category_id = sub_category_id
            if og_price != '':
                product.og_price = og_price
            if member_price != '':
                product.member_price = member_price
        else:
            print(f"Failed to update product with ID {product_id}.")
    
from DbHelper import DbHelper as db


class Inventory:
    def __init__(self):
        self.__categories, self.__subcategories = db.get_all_categories()
        self.__products = db.get_all_products(self.__subcategories)

    @property
    def products(self):
        return db.get_all_products(self.__subcategories)
        #return self.__products

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
        """
        Update a product in the inventory.

        Parameters:
        - product_id (str): The ID of the product to be updated.
        - name (str): The new name of the product. Leave blank to keep the current name.
        - brand (str): The new brand of the product. Leave blank to keep the current brand.
        - description (str): The new description of the product. Leave blank to keep the current description.
        - quantity (str): The new quantity of the product. Leave blank to keep the current quantity.
        - sub_category_id (str): The new sub-category ID of the product. Leave blank to keep the current sub-category ID.
        - og_price (str): The new original price of the product. Leave blank to keep the current original price.
        - member_price (str): The new member price of the product. Leave blank to keep the current member price.

        """
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
            print("The latest information for this item is\n",product)
        else:
            print(f"Failed to update product with ID {product_id}.")
    
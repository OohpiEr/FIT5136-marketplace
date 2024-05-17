import csv
from domain import Product
from domain import Category
from domain import SubCategory
from RowNotFoundError import RowNotFoundError


class DbHelper:
    """Static Database helper class. Used to connect to the physical database.

    :raises RowNotFoundError: Raised when the row is not found in the database
    """
    DB_PATH = "db"
    CATEGORY_TBL_FILE_NAME = "category.txt"
    CUSTOMER_TBL_FILE_NAME = "customer.txt"
    PRODUCT_TBL_FILE_NAME = "product.txt"
    SUBCATEGORY_TBL_FILE_NAME = "subcategory.txt"
    USER_TBL_FILE_NAME = "user.txt"

    @classmethod
    def __get_data(self, filename):
        """Gets the data from a csv file

        :param filename: filename
        :return: a list of dictionary objects containing the data in the file
        """
        with open(f"{self.DB_PATH}/{filename}", mode="r", encoding="UTF-8") as f:
            data = list(csv.DictReader(f, delimiter=','))
            return data

    @classmethod
    def __get_subcategory(self, subcategory_id, subcategories):
        """Gets the subcategory object from the inventory.

        :param subcategory_id: subcategory id
        :param subcategories: list of subcategory objects in the inventory
        :return: subcategory object
        """
        subcategory = None
        for subcat in subcategories:
            if subcategory_id == subcat.id:
                subcategory = subcat

        return subcategory

    @classmethod
    def get_all_products(self, subcategories):
        """Gets all products from the database

        :param subcategories: list of subcategories in the inventory
        :raises RowNotFoundError: raised when the row is not found
        :return: list of product objects in the database
        """
        product_dict_list = self.__get_data(self.PRODUCT_TBL_FILE_NAME)
        products = []

        for product_dict in product_dict_list:
            # product_id, name, brand, description, quantity, sub_category, og_price, member_price
            subcategory = self.__get_subcategory(
                int(product_dict['subcat_id']), subcategories)

            if subcategory == None:
                raise RowNotFoundError("Subcategory not found.")

            product = Product.Product(
                product_dict['product_id'],
                product_dict['product_name'],
                product_dict['product_brand'],
                product_dict['product_desc'],
                product_dict['product_qty'],
                subcategory,
                product_dict['product_og_price'],
                product_dict['product_member_price'],
            )
            products.append(product)

        return products

    @classmethod
    def get_all_categories(self):
        """Gets all the categories in the database

        :return: list of category objects
        """
        cat_dict_list = self.__get_data(self.CATEGORY_TBL_FILE_NAME)
        subcat_dict_list = self.__get_data(self.SUBCATEGORY_TBL_FILE_NAME)
        subcategories = []
        categories = []
        cat_id_index_map = [None] * (int(cat_dict_list[-1]['cat_id']) + 1)

        for i, dict in enumerate(cat_dict_list):
            cat_id = int(dict['cat_id'])

            category = Category.Category(
                cat_id,
                dict['cat_name']
            )
            # id, name
            cat_id_index_map[cat_id] = i
            categories.append(category)

        for dict in subcat_dict_list:
            category = categories[cat_id_index_map[int(dict['cat_id'])]]

            subcategory = SubCategory.SubCategory(
                int(dict['subcat_id']),
                dict['subcat_name'],
                category
            )

            category.add_subcategory(subcategory)
            subcategories.append(subcategory)

        return (categories, subcategories)

    @classmethod
    def __get_new_id(self, file):
        """Gets the new id for a table (csv file)

        :param file: filename string    
        :return: new integer id of the table
        """
        *_, last_row = csv.reader(file, delimiter=',')
        new_id = int(last_row[0]) + 1
        return new_id

    @classmethod
    def add_product(self, name, brand, description, quantity, subcategory_id, og_price, member_price, subcategories):
        """Add a product to the database

        :param subcategories: _description_
        :param name: product name
        :param brand: product brand
        :param description: product description
        :param quantity: product quantity
        :param subcategory_id: product subcategory id
        :param og_price: product price
        :param member_price: product member price
        :raises RowNotFoundError: raised when row is not found in the database
        :return: product object of the product added
        """
        subcategory = self.__get_subcategory(subcategory_id, subcategories)

        if subcategory == None:
            raise RowNotFoundError("Subcategory not found.")

        with open(f"{self.DB_PATH}/{self.PRODUCT_TBL_FILE_NAME}", 'r+', newline="") as f:
            product_id = self.__get_new_id(f)
            product = Product.Product(
                product_id, name, brand, description, quantity, subcategory, og_price, member_price)

            writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([product_id, name, product.brand, description,
                            quantity, og_price, member_price, subcategory_id])

            return product

    @classmethod
    def delete_product(self, product_id):
        """Delete a product from the database

        :param product_id: product id to be deleted
        :raises RowNotFoundError: raised when product is not found in the database
        """
        deleted = False
        prod_list = []
        with open(f"{self.DB_PATH}/{self.PRODUCT_TBL_FILE_NAME}", 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            # lines = f.readlines()
            for line in reader:
                if line[0] != str(product_id):
                    prod_list.append(line)
                    # f.write(line)
                else:
                    deleted = True

            f.seek(0)
            writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(prod_list)

            f.truncate()

        if not deleted:
            raise RowNotFoundError

    @classmethod
    def update_product(cls, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None,
                       og_price=None, member_price=None):
        # read the origin data
        data = cls.__get_data(cls.PRODUCT_TBL_FILE_NAME)

        # find the index
        index = None
        for i, row in enumerate(data):
            if row['product_id'] == product_id:
                index = i
                break

        # if the product exists
        if index is not None:
            # update information
            if name != '':
                data[index]['product_name'] = name
            if brand != '':
                data[index]['product_brand'] = brand
            if description != '':
                data[index]['product_desc'] = description
            if quantity != '':
                data[index]['product_qty'] = quantity
            if sub_category_id != '':
                data[index]['subcat_id'] = sub_category_id
            if og_price != '':
                data[index]['product_og_price'] = og_price
            if member_price != '':
                data[index]['product_member_price'] = member_price

            # write in the file
            with open(f"{cls.DB_PATH}/{cls.PRODUCT_TBL_FILE_NAME}", mode="w", newline='', encoding="UTF-8") as f:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

            return True
        return False

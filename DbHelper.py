import csv
from domain import Product
from RowNotFoundError import RowNotFoundError


class DbHelper:
    db_path = "db"
    CATEGORY_TBL_FILE_NAME = "category.txt"
    CUSTOMER_TBL_FILE_NAME = "customer.txt"
    FOODPRODUCT_TBL_FILE_NAME = "foodproduct.txt"
    PRODUCT_TBL_FILE_NAME = "product.txt"
    SUBCATEGORY_TBL_FILE_NAME = "subcategory.txt"
    USER_TBL_FILE_NAME = "user.txt"

    @classmethod
    def __get_data(self, filename):
        with open(f"{self.db_path}/{filename}", mode="r", encoding="UTF-8") as f:
            data = list(csv.DictReader(f, delimiter=','))
            return data

    @classmethod
    def get_all_products(self):
        return self.__get_data(self.PRODUCT_TBL_FILE_NAME)


    @classmethod
    def get_all_foodproduct(self):
        return self.__get_data(self.FOODPRODUCT_TBL_FILE_NAME)

    @classmethod
    def __get_new_id(self, file):
        # https://stackoverflow.com/questions/2138873/cleanest-way-to-get-last-item-from-python-iterator
        *_, last_row = csv.reader(file, delimiter=',')
        new_id = int(last_row[0]) + 1
        return new_id
    
    @classmethod
    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        with open(f"{self.db_path}/{self.PRODUCT_TBL_FILE_NAME}", 'r+',newline="") as f:
            product_id = self.__get_new_id(f)
            product = Product.Product(product_id, name, brand, description, quantity, sub_category_id, og_price, member_price)

            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([product_id, name, product.brand, description, quantity, sub_category_id, og_price, member_price])

            return product
    
    @classmethod
    def delete_product(self, product_id):
        deleted = False
        prod_list = []
        with open(f"{self.db_path}/{self.PRODUCT_TBL_FILE_NAME}", 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            # lines = f.readlines()
            for line in reader:
                if line[0] != str(product_id):
                    prod_list.append(line)
                    # f.write(line)
                else:
                    deleted = True
            
            f.seek(0)
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(prod_list)
            
            f.truncate()
        
        if not deleted:
            raise RowNotFoundError

    @classmethod
    def update_product(self, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None,
                       og_price=None, member_price=None):
        # read the origin data
        data = self.get_all_products()

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

            print("The latest information for this item is: ",data[index])
            # write in the file
            with open(f"{self.db_path}/{self.PRODUCT_TBL_FILE_NAME}", mode="w", newline='', encoding="UTF-8") as f:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

            print("Product updated successfully.")
        else:
            print(f"Product with ID {product_id} not found.")


if __name__ == "__main__":
    db = DbHelper()
    # p = Product.Product(7, "name", "brand", "description", 10, 6.9, 5, 11)
    db.delete_product(5)
    # db.add_product("Colgate Total Charcoal Deep Clean Toothpaste", "Colgate",
                #    "Colgate Total Antibacterial Fluoride toothpaste has a unique formula that keeps your whole mouth healthy by fighting bacteria on teeth, tongue, cheeks, and gums for 12 hours*. Colgate Total Charcoal Deep Clean, active cleaning formula fights plaque even between teeth and hard to reach spaces", 10, 6.9, 5, 11)

import csv
from domain import Product


class DbHelper:
    db_path = "db"
    category_tbl_file_name = "category.txt"
    customer_tbl_file_name = "customer.txt"
    foodproduct_tbl_file_name = "foodproduct.txt"
    product_tbl_file_name = "product.txt"
    subcategory_tbl_file_name = "subcategory.txt"
    user_tbl_file_name = "user.txt"

    def get_data(self, filename):
        with open(f"{self.db_path}/{filename}", mode="r", encoding="UTF-8") as f:
            data = list(csv.DictReader(f, delimiter=','))
            return data

    def get_all_products(self):
        return self.get_data(self.product_tbl_file_name)

    def get_all_foodproduct(self):
        return self.get_data(self.foodproduct_tbl_file_name)

    def get_new_id(self, file):
        # https://stackoverflow.com/questions/2138873/cleanest-way-to-get-last-item-from-python-iterator
        *_, last_row = csv.reader(file, delimiter=',')
        new_id = int(last_row[0]) + 1
        return new_id

    def add_product(self, name, brand, description, quantity, sub_category_id, og_price, member_price):
        with open(f"{self.db_path}/{self.product_tbl_file_name}", 'r+', newline='') as f:
            product_id = self.get_new_id(f)
            product = Product.Product(product_id, name, brand, description, quantity, sub_category_id, og_price, member_price)

            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([product_id, name, product.brand, description, quantity, sub_category_id, og_price, member_price])

            return product
    
    # def delete_product(self, product):

    def update_product(self, product_id, name=None, brand=None, description=None, quantity=None, sub_category_id=None,
                       og_price=None, member_price=None):
        # 读取原始数据
        data = self.get_all_products()

        # 找到要更新的产品在数据中的索引
        index = None
        for i, row in enumerate(data):
            if int(row['id']) == product_id:
                index = i
                break

        # 如果找到了产品
        if index is not None:
            # 更新产品信息
            if name is not None:
                data[index]['name'] = name
            if brand is not None:
                data[index]['brand'] = brand
            if description is not None:
                data[index]['description'] = description
            if quantity is not None:
                data[index]['quantity'] = quantity
            if sub_category_id is not None:
                data[index]['sub_category_id'] = sub_category_id
            if og_price is not None:
                data[index]['og_price'] = og_price
            if member_price is not None:
                data[index]['member_price'] = member_price

            # 写入更新后的数据到文件
            with open(f"{self.db_path}/{self.product_tbl_file_name}", mode="w", newline='', encoding="UTF-8") as f:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

            print("Product updated successfully.")
        else:
            print(f"Product with ID {product_id} not found.")


if __name__ == "__main__":
    db = DbHelper()
    db.add_product("Colgate Total Charcoal Deep Clean Toothpaste", "Colgate",
                   "Colgate Total Antibacterial Fluoride toothpaste has a unique formula that keeps your whole mouth healthy by fighting bacteria on teeth, tongue, cheeks, and gums for 12 hours*. Colgate Total Charcoal Deep Clean, active cleaning formula fights plaque even between teeth and hard to reach spaces", 10, 6.9, 5, 11)

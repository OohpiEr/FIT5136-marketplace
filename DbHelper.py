import csv
# import Product


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

    def add_product(self, product):
        with open(f"{self.db_path}/{self.product_tbl_file_name}", 'r+', newline='') as f:
            writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([self.get_new_id(f), product.name, product.brand, product.description, product.quantity,
                            product.og_price, product.member_price, product.sub_category_id])


if __name__ == "__main__":
    db = DbHelper()
    db.add_product("Colgate Total Charcoal Deep Clean Toothpaste", "Colgate",
                   "Colgate Total Antibacterial Fluoride toothpaste has a unique formula that keeps your whole mouth healthy by fighting bacteria on teeth, tongue, cheeks, and gums for 12 hours*. Colgate Total Charcoal Deep Clean, active cleaning formula fights plaque even between teeth and hard to reach spaces", 10, 6.9, 5, 11)

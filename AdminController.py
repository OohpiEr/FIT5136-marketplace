from UserInputError import UserInputError
from AdminInterface import AdminInterface
from RowNotFoundError import RowNotFoundError
from domain.Admin import Admin


class AdminController():
    """Controller class for administration interface. Contains logic for admin interface."""

    def __init__(self, inventory):
        """Constructor

        :param inventory: inventory object for the application
        """
        self.ui = AdminInterface()
        self.admin = Admin(inventory)

    def admin_control(self):
        """Starting point of the admin interface. Displays the admin home menu

        :raises UserInputError: Error when the user input is invalid
        """
        # [("1","Add Item"), ("2", "Delete Item"), ("3", "Edit Item"), ("q", "Quit")]
        quit_flag = False
        display_menu = True
        while not quit_flag:
            if display_menu:
                self.ui.display_home()

            admin_choice = input().strip().lower()

            try:
                if len(admin_choice) == 0:
                    raise UserInputError

                match admin_choice:
                    case "1":
                        self.add_product()
                        display_menu = True
                    case "2":
                        self.delete_product()
                        display_menu = True
                    case "3":
                        self.update_product()
                        display_menu = True
                    case '4':
                        self.borwse_item()
                        display_menu = True
                    case "q":
                        return
                    case _:
                        display_menu = False
                        raise UserInputError
            except UserInputError as e:
                self.ui.display_result_msg("Invalid input.")

    def delete_product(self):
        """Logic for the delete product functionality."""
        product_id = input(
            "Please enter the product ID you wish to delete: ").strip()
        msg = ""

        try:
            product_id = int(product_id)
            self.admin.delete_product(product_id)
            msg = f"Product {product_id} deleted."
        except RowNotFoundError as e:
            msg = "Product ID not found."
        except Exception as e:
            msg = "Invalid product ID."

        self.ui.display_result_msg(msg)

    def update_product(self):
        self.admin.show_product()
        product_id = input(
            "Please enter the product ID you wish to update: ").strip()
        name = input("Enter new name (leave blank to keep current): ").strip()
        brand = input(
            "Enter new brand (leave blank to keep current): ").strip()
        description = input(
            "Enter new description (leave blank to keep current): ").strip()
        quantity = input(
            "Enter new quantity (leave blank to keep current): ").strip()
        sub_category_id = input(
            "Enter new sub-category ID (leave blank to keep current): ").strip()
        og_price = input(
            "Enter new original price (leave blank to keep current): ").strip()
        member_price = input(
            "Enter new member price (leave blank to keep current): ").strip()
        self.admin.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price,
                                  member_price)

    def add_product(self):
        """Logic for adding products.

        :raises UserInputError: Error when user input is invalid
        """
        name = input(
            "Please enter the name of the product you wish to add: ").strip()
        brand = input("Please enter the brand of the product: ").strip()
        description = input("Please enter the product description: ").strip()
        quantity = input(
            "Please enter the quantity of the product you wish to add: ").strip()
        sub_category_id = input(
            "Please enter the sub-category of the item you wish to add: ").strip()
        og_price = input(
            "Please input the full price for the product: ").strip()
        member_price = input(
            "Please enter the membership price of the product available to members: ").strip()

        try:
            product = self.admin.add_product(name, brand, description, int(
                quantity), int(sub_category_id), float(og_price), float(member_price))
        except ValueError as e:
            raise UserInputError

        self.ui.display_result_msg(f"Product added:\n" + str(product))

    def borwse_item(self):
        self.admin.show_product()
        # print(" Please input the way of browse item:")
        # product_title = []
        # product_list = []
        # category_list = []
        # category_title = []
        # print(
        #     "     [1]category\n     [2]brand\n     [3]view all items\n     [4]Quit\n")
        # with open('db/product.txt', 'r') as f:
        #     product_title = f.readline().replace("\n", "").split(",")
        #     item = f.readline().replace("\n", "")
        #     while len(item) > 0:
        #         product_list.append(item.split(","))
        #         item = f.readline().replace("\n", "")
        # with open('db/subcategory.txt', 'r') as f:
        #     category_title = f.readline().replace("\n", "").split(",")
        #     item = f.readline()
        #     while len(item) > 0:
        #         category_list.append(item.replace("\n", "").split(","))
        #         item = f.readline().replace("\n", "")
        # check_type = input(" Enter your choice:")
        # if check_type == '1':
        #     category_id = None
        #     category_name = input("Please input the category:")
        #     for category_item in category_list:
        #         if category_item[1] == category_name:
        #             category_id = category_item[0]
        #             break
        #     if category_id != None:
        #         output_data = []
        #         for item in product_list:
        #             if item[-1] == category_id:
        #                 print(output_data.append([item[i] for i in [0, 1, 4]]))
        #         if len(output_data) > 0:
        #             print("\t".join([product_title[i] for i in [0, 1, 4]]))
        #             for item in output_data:
        #                 print("\t".join(item))
        #         else:
        #             print("There is no product!")
        # elif check_type == '2':
        #     output_data = []
        #     index = product_title.index("product_brand")
        #     brand_name = input("Please input the brand:")
        #     for item in product_list:
        #         if item[index] == brand_name:
        #             output_data.append([item[i] for i in [0, 1, 4]])
        #     if len(output_data) > 0:
        #         print("\t".join([product_title[i] for i in [0, 1, 4]]))
        #         for item in output_data:
        #             print("\t".join(item))
        #     else:
        #         print("There is no product!")
        # elif check_type == '3':
        #     print("\t".join([product_title[i] for i in [0, 1, 4]]))
        #     for item in product_list:
        #         print("\t".join([item[i] for i in [0, 1, 4]]))
        # elif check_type == '4':
        #     return

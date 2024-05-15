from UserInputError import UserInputError
from AdminInterface import AdminInterface
from RowNotFoundError import RowNotFoundError
from domain.Admin import Admin


class AdminController():
    def __init__(self, inventory):
        # super().__init__()
        self.ui = AdminInterface()
        self.admin = Admin(inventory)

    def home_page(self):
        self.ui.display_home()
        inp = input("Input: ")
        print(inp)

    # def admin_control1(self):
    #     admin_obj = Admin()
    #     admin_message = "Please choose an Administrator action: "

    #     while True:
    #         admin_choice = input(admin_message).strip().upper()
    #         if admin_choice == "1":
    #             name = input("Please enter the name of the product you wish to add: ")
    #             brand = input("Please enter the brand of the product: ")
    #             description = input("Please enter the product description: ")
    #             quantity = input("Please enter the quantity of the product you wish to add: ")
    #             sub_category_id = input("Please enter the sub-category of the item you wish to add: ")
    #             og_price = input("Please input the full price for the product: ")
    #             member_price = input("Please enter the membership price of the product available to members: ")
    #             admin_obj.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)
    #         elif admin_choice == "2":
    #             print("need to be done")
    #         elif admin_choice == "3":
    #             product_id = input("Please enter the product ID you wish to update: ")
    #             name = input("Enter new name (leave blank to keep current): ")
    #             brand = input("Enter new brand (leave blank to keep current): ")
    #             description = input("Enter new description (leave blank to keep current): ")
    #             quantity = input("Enter new quantity (leave blank to keep current): ")
    #             sub_category_id = input("Enter new sub-category ID (leave blank to keep current): ")
    #             og_price = input("Enter new original price (leave blank to keep current): ")
    #             member_price = input("Enter new member price (leave blank to keep current): ")
    #             admin_obj.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price,
    #                                      member_price)
    #         elif admin_choice == "Q":
    #             break
    #         else:
    #             print("Invalid input. Please enter 1, 2, 3 to perform an action or 'Q' to quit.")

    def admin_control(self):
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
                    case "q":
                        return
                    case _:
                        display_menu = False
                        raise UserInputError
            except UserInputError as e:
                print("Invalid input. Please enter 1, 2, 3 to perform an action or 'q' to quit.")

    def delete_product(self):
        product_id = input("Please enter the product ID you wish to delete: ").strip()
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
        product_id = input("Please enter the product ID you wish to update: ")
        name = input("Enter new name (leave blank to keep current): ")
        brand = input("Enter new brand (leave blank to keep current): ")
        description = input("Enter new description (leave blank to keep current): ")
        quantity = input("Enter new quantity (leave blank to keep current): ")
        sub_category_id = input("Enter new sub-category ID (leave blank to keep current): ")
        og_price = input("Enter new original price (leave blank to keep current): ")
        member_price = input("Enter new member price (leave blank to keep current): ")
        self.admin.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price,
                                 member_price)
        # product_id = input("Please enter the product ID you wish to update: ").strip()
        # name = input("Enter new name (leave blank to keep current): ").strip()
        # brand = input("Enter new brand (leave blank to keep current): ").strip()
        # description = input("Enter new description (leave blank to keep current): ").strip()
        # quantity = input("Enter new quantity (leave blank to keep current): ").strip()
        # sub_category_id = input("Enter new sub-category ID (leave blank to keep current): ").strip()
        # og_price = input("Enter new original price (leave blank to keep current): ").strip()
        # member_price = input("Enter new member price (leave blank to keep current): ").strip()
        #
        # try:
        #     product_id = int(product_id)
        #     self.admin.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price, member_price)
        #     msg = f"Product {product_id} updated."
        # except RowNotFoundError as e:
        #     msg = "Product ID not found."
        # except Exception as e:
        #     msg = "Invalid product ID."
        #
        # self.ui.display_result_msg(msg)

    def add_product(self):
        name = input("Please enter the name of the product you wish to add: ").strip()
        brand = input("Please enter the brand of the product: ").strip()
        description = input("Please enter the product description: ").strip()
        quantity = input("Please enter the quantity of the product you wish to add: ").strip()
        sub_category_id = input("Please enter the sub-category of the item you wish to add: ").strip()
        og_price = input("Please input the full price for the product: ").strip()
        member_price = input("Please enter the membership price of the product available to members: ").strip()
        product = self.admin.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)

        self.ui.display_result_msg(f"Product added:\n" + str(product))
        

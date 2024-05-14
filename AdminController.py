from UserInputError import UserInputError
from AdminInterface import AdminInterface
from domain.Admin import Admin


class AdminController():
    def __init__(self):
        # super().__init__()
        self.ui = AdminInterface()
        self.admin = Admin()

    # def handle_input(self, input):

    def home_page(self):
        self.ui.display_home()
        inp = input("Input: ")
        print(inp)

    def admin_control(self):
        # [("1","Add Item"), ("2", "Delete Item"), ("3", "Edit Item"), ("q", "Quit")]
        self.ui.display_home()
        quit_flag = False
        while not quit_flag:
            admin_choice = input().strip().lower()

            try:
                if len(admin_choice) == 0:
                    raise UserInputError

                match admin_choice:
                    case "1":
                        self.add_product()
                    case "2":
                        # Delete Item
                        pass
                    case "3":
                        self.update_product()
                    case "q":
                        return
                    case _:
                        raise UserInputError
            except UserInputError as e:
                print(
                    "Invalid input. Please enter 1, 2, 3 to perform an action or 'q' to quit.")

    def update_product(self):
        product_id = input(
            "Please enter the product ID you wish to update: ").strip()
        name = input(
            "Enter new name (leave blank to keep current): ").strip()
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
        self.admin.add_product(name, brand, description, quantity,
                               sub_category_id, og_price, member_price)

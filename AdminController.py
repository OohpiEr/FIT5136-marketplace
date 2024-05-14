from UserInputError import UserInputError
from AdminInterface import AdminInterface
from domain.Admin import Admin

class AdminController():
    def __init__(self):
        # super().__init__()
        self.ui = AdminInterface()
        
    # def handle_input(self, input):
        
    def home_page(self):
        self.ui.display_home()
        inp = input("Input: ")
        print(inp)
    
    def admin_control(self):
        options = self.ui.display_home()
        admin_obj = Admin()
        admin_message = "Please choose an Administrator action: "
        quit_flag = False
        while not quit_flag:
            admin_choice = input(admin_message).strip().lower()
            
            try:
                if len(admin_choice) == 0 or admin_choice not in options: 
                    raise UserInputError
                
                match admin_choice:
                    case "1":
                        name = input("Please enter the name of the product you wish to add: ")
                        brand = input("Please enter the brand of the product: ")
                        description = input("Please enter the product description: ")
                        quantity = input("Please enter the quantity of the product you wish to add: ")
                        sub_category_id = input("Please enter the sub-category of the item you wish to add: ")
                        og_price = input("Please input the full price for the product: ")
                        member_price = input("Please enter the membership price of the product available to members: ")
                        admin_obj.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)
                    case "3":
                        product_id = input("Please enter the product ID you wish to update: ")
                        name = input("Enter new name (leave blank to keep current): ")
                        brand = input("Enter new brand (leave blank to keep current): ")
                        description = input("Enter new description (leave blank to keep current): ")
                        quantity = input("Enter new quantity (leave blank to keep current): ")
                        sub_category_id = input("Enter new sub-category ID (leave blank to keep current): ")
                        og_price = input("Enter new original price (leave blank to keep current): ")
                        member_price = input("Enter new member price (leave blank to keep current): ")
                        admin_obj.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price,
                                                member_price)
                    case "q":
                        break
            except UserInputError as e:
                print("Invalid input. Please enter 1, 2, 3 to perform an action or 'Q' to quit.")
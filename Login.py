from UserInterface import UserInterface
from AdminController import AdminController
from domain.Admin import Admin
from domain.Customer import Customer
import csv


class Login:
    def __init__(self):
        pass

    def login_control(self):
        admin_email = "admin@merchant.monash.edu"
        customer_email = "member@student.monash.edu"
        main_choice = "Enter your choice, or 'Q' to Quit: "
        wrong_choice = "Please enter a valid menu option"
        incorrect_login = "Your entered details are not the correct email or password"
        
        ui_obj = UserInterface()
        ui_obj.display_landing_page()
        
        user_choice = input(main_choice)
        if user_choice[0] != "1" or user_choice[0] != "Q" or user_choice[0] == "" or user_choice[0] == " ":
            print(wrong_choice)
            user_choice = input(main_choice)
        if user_choice[0] == "1":
            user_choice_email = input("      # Email: ")
            user_choice_password = input("      # Password: ")
            strip_username = user_choice_email.strip(" ")
            login_attempt = self.login(strip_username, user_choice_password)
            try:
                all_user_data = []
                with open("db/user.txt", "r", encoding="UTF-8") as file_2:
                    read_all_lines = file_2.read().split("\n")
                    for lines in read_all_lines:
                        all_user_data.append(lines)
                        for lines_2 in all_user_data:
                            if login_attempt and user_choice_email == admin_email:
                                # ui_obj.display_admin_menu()
                                # self.admin_control()
                                admin_controller = AdminController()
                                admin_controller.admin_control()
                                self.login_control()
                            elif not login_attempt:
                                print(incorrect_login)
                                self.login_control()
                            else:
                                if login_attempt and user_choice_email == customer_email:
                                    ui_obj.display_customer_menu()
                                    self.customer_control()
                                    self.login_control()
            except FileNotFoundError:
                print("'user.txt' does not exist in system. Please create the file")
            except IOError:
                print("Error opening and reading from file. Make sure it exists")
            except EOFError:
                print("No data found in the file. Please check contents")


    def login(self, username, password):
        admin_email_2 = "admin@merchant.monash.edu"
        customer_email_2 = "member@student.monash.edu"
        admin_password_2 = "12345678"
        customer_password_2 = "Monash1234"
        login_info = []
        try:
            with open("db/user.txt", "r", encoding="UTF-8") as file_1:
                data = file_1.read().split("\n")
                for lines in data:
                    login_info.append(lines)
                    for line in login_info:
                        if username == admin_email_2 and password == admin_password_2 or username == customer_email_2 and password == customer_password_2:
                            return line
                        elif username != admin_email_2 and password != admin_password_2 or username != customer_email_2 and password != customer_password_2:
                            return None
        except FileNotFoundError:
            print("'user.txt' does not exist in system. Please create the file")
        except IOError:
            print("Error opening and reading from file. Make sure it exists")
        except EOFError:
            print("No data found in the file. Please check contents")

    # def admin_control(self):
    #     admin_obj = Admin()
    #     admin_message = "Please choose an Administrator action: "
    #     # admin_choice = input(admin_message)
    #     quit_flag = False
    #     while not quit_flag:
    #         admin_choice = input(admin_message).strip()
            
    #         try:
    #             temp = admin_choice not in ["1", "2", "3", "Q","q"]
    #             if admin_choice[0] not in ["1", "2", "3", "Q","q"]: 
    #                 raise UserInputError
                    
    #             if admin_choice == "1":
    #                 name = input("Please enter the name of the product you wish to add: ")
    #                 brand = input("Please enter the brand of the product: ")
    #                 description = input("Please enter the product description: ")
    #                 quantity = input("Please enter the quantity of the product you wish to add: ")
    #                 sub_category_id = input("Please enter the sub-category of the item you wish to add: ")
    #                 og_price = input("Please input the full price for the product: ")
    #                 member_price = input("Please enter the membership price of the product available to members: ")
    #                 admin_obj.add_product(name, brand, description, quantity, sub_category_id, og_price, member_price)
    #             elif admin_choice == "3":
    #                 product_id = input("Please enter the product ID you wish to update: ")
    #                 name = input("Enter new name (leave blank to keep current): ")
    #                 brand = input("Enter new brand (leave blank to keep current): ")
    #                 description = input("Enter new description (leave blank to keep current): ")
    #                 quantity = input("Enter new quantity (leave blank to keep current): ")
    #                 sub_category_id = input("Enter new sub-category ID (leave blank to keep current): ")
    #                 og_price = input("Enter new original price (leave blank to keep current): ")
    #                 member_price = input("Enter new member price (leave blank to keep current): ")
    #                 admin_obj.update_product(product_id, name, brand, description, quantity, sub_category_id, og_price,
    #                                         member_price)
    #             elif admin_choice == "Q":
    #                 break
    #         except UserInputError as e:
    #             print("Invalid input. Please enter 1, 2, 3 to perform an action or 'Q' to quit.")
                

    def customer_control(self):
        cust_message = "Please choose a Customer action: "
        cust_choice = input(cust_message)
        cust_obj = Customer()
        while cust_choice[0] != "Q" or cust_choice[0] == "" or cust_choice == " ":
            print("Put customer menu choices here")
            cust_choice = input(cust_message)
            if cust_choice[0] == "1":
                with open('db/product.txt', 'r') as f3:
                    reader2 = csv.reader(f3)
                    for line in reader2:
                        print("Browsing all products: ")
                        print(line)
                        add = input("You may add items to cart whilst browsing. Enter 'Add' to start adding: ")
                        if add[0] == "Add":
                            cust_obj.add_product_to_cart()
            if cust_choice[0] == "Q":
                break

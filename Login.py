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


        while True:
            user_choice = input(main_choice).strip().upper()
            if user_choice == "1":
                user_choice_email = input("      # Email: ").strip()
                user_choice_password = input("      # Password: ").strip()
                login_attempt = self.login(user_choice_email, user_choice_password)

                if login_attempt:
                    if user_choice_email == admin_email:
                        admin_interface = AdminController()
                        admin_interface.admin_control()
                        #self.admin_control()
                    elif user_choice_email == customer_email:
                        ui_obj.display_customer_menu()
                        self.customer_control()
                    break  # 登录成功，退出循环
                else:
                    print(incorrect_login)
            elif user_choice == "Q":
                break  # 用户选择退出，退出循环
            else:
                print(wrong_choice)



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

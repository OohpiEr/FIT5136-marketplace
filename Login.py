"""
Group Number: 4
Group Members: Margaret Tai, Tian Er Ru, Mingzhu Qian, Jialin Zhong

This class's functionality is to provide the Monash Merchant Online Shopping Website with the ability
to login as a Customer or Administrator, to perform certain tasks such as browse items, manage inventory,
and manage purchases through an online shopping portal for students and staff. The login control function
acts as the access control for logging into the website to access accounts and manage such inventory
or purchases to fulfil the purpose of the Monash Merchant Marketplace. The login takes two inputs:
email and password, and verifies whether the account user/holder exists in the database, to be able to login
safely and securely to the owner's account. The only users are an administrator and customer, from which
will use credentials from the provided information.

Administrator email: admin@merchant.monash.edu
Administrator password: 12345678

Customer email: member@student.monash.edu
Customer password: Monash1234

"""


from UserInterface import UserInterface
from AdminController import AdminController
from CustomerController import CustomerController
# from domain.Admin import Admin
# from domain.Customer import Customer
# import csv


class Login:
    def __init__(self):
        pass

    def login_control(self, inventory):
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
                        admin_controller = AdminController(inventory)
                        admin_controller.admin_control()
                    elif user_choice_email == customer_email:
                        # ui_obj.display_customer_menu()
                        # self.customer_control()
                        cust_controller = CustomerController(inventory)
                        cust_controller.customer_control()
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





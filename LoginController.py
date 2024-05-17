"""
Group Number: 4
Group Members: Margaret Tai, Tian Ru Er, Mingzhu Qian, Jialin Zhong

This class's functionality is to provide the Monash Merchant Online Shopping Website with the ability
to login as a Customer or Administrator, to perform certain tasks such as browse items, manage inventory,
and manage purchases through an online shopping portal for students and staff. The login control function
acts as the access control for logging into the website to access accounts and manage such inventory
or purchases to fulfil the purpose of the Monash Merchant Marketplace. The login takes two inputs:
email and password, and verifies whether the account user/holder exists in the database, to be able to login
safely and securely to the owner's account. The only users are an administrator and customer, from which
will use credentials from the provided information.
"""


from UserInterface import UserInterface
from AdminController import AdminController
from CustomerController import CustomerController


class LoginController:
    def __init__(self):
        pass

    def login_control(self, users):
        """Control block for login. Contains the logic for the login screen

        :param users: list of user objects
        """
        user_prompt = "Enter your choice, or 'q' to Quit: "
        wrong_choice = "Please enter a valid menu option"
        incorrect_login = "Your entered details are not the correct email or password"

        ui_obj = UserInterface()

        while True:
            ui_obj.display_landing_page()
            user_choice = input(user_prompt).strip().lower()
            
            if user_choice == "1":
                user_choice_email = input("      # Email: ").strip()
                user_choice_password = input("      # Password: ").strip()
                
                user = None
                for cur_user in users:
                    if user_choice_email == cur_user.email and user_choice_password == cur_user.password:
                        user = cur_user
                        break
                if user is not None:
                    match user.id:
                        case 1:
                            admin_controller = AdminController(cur_user)
                            admin_controller.admin_control()
                        case 2:
                            cust_controller = CustomerController(cur_user)
                            cust_controller.customer_control()
                        case _:
                            print(incorrect_login)
                else:
                    print(incorrect_login)
            elif user_choice == "q":
                break
            else:
                print(wrong_choice)


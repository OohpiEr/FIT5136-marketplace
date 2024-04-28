from user_interface import UserInterface


class Login:
    def __init__(self):
        pass

    def login_control(self):
        admin_email = "admin@merchant.monash.edu"
        customer_email = "member@student.monash.edu"
        main_choice = "Enter your choice, or 'Q' to Quit: "
        wrong_choice = "Please enter a valid menu option"
        ui_obj = UserInterface()
        ui_obj.display_landing_page()
        user_choice = input(main_choice)
        if user_choice[0] == "" or user_choice[0] == " ":
            print(wrong_choice)
            user_choice = input(main_choice)
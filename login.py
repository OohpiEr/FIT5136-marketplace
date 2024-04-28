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
        if user_choice[0] == "1":
            user_choice_email = input("      # Email: ")
            user_choice_password = input("      # Password: ")
            strip_username = user_choice_email.strip(" ")

    def login(self, username, password):
        admin_email_2 = "admin@merchant.monash.edu"
        customer_email_2 = "member@student.monash.edu"
        admin_password_2 = "12345678"
        customer_password_2 = "Monash1234"
        login_info = []
        try:
            with open("users_file.txt", "r", encoding="UTF-8") as file_1:
                data = file_1.read().split("\n")
                for lines in data:
                    login_info.append(lines)
                    for line in login_info:
                        if username == admin_email_2 and password == admin_password_2 or username == customer_email_2 and password == customer_password_2:
                            return line
                        elif username != admin_email_2 and password != admin_password_2 or username != customer_email_2 and password != customer_password_2:
                            return None
        except FileNotFoundError:
            print("'users_file.txt' does not exist in system. Please create the file")
        except IOError:
            print("Error opening and reading from file. Make sure it exists")
        except EOFError:
            print("No data found in the file. Please check contents")
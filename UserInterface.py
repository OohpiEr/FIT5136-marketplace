class UserInterface():
    """User interface class for displaying the user interface"""
    TAB = "     "
    OPTION_PROMPT = "PLEASE SELECT AN OPTION"
    INPUT_PROMPT = "INPUT:"
    NEWLINE = "\n"
    QUIT_OPTION = ("q", "Quit")

    def display_result_msg(self, msg):
        """Display the result message. Waits for user input to continue

        :param msg: message to display
        """
        print(self.NEWLINE, self.NEWLINE, msg, self.NEWLINE, self.NEWLINE)
        input("Enter to continue...")

    def display_landing_page(self):
        """Displays the landing page"""
        print("  _||____________________________________________||_")
        print("(__  ____________________________________________  __)")
        print("   ||                                            ||")
        print("   ||                -- WELCOME --               ||")
        print("   ||                     TO                     ||")
        print("   ||                 MONASH SHOP                ||")
        print("   ||                                            ||")
        print("   ||                                            ||")
        print("   ||                                            ||")
        print("  _||____________________________________________||_")
        print("(__  ____________________________________________  __)")
        print("   ||                                            ||")
        print("")
        print("")
        print("     PLEASE SELECT AN OPTION")
        print("       [1] Login")
        print("")
        print("")

    def display_login_page(self):
        """Displays the login page"""
        print(" _____________________________________________________")
        print("|  _________________________________________________  |")
        print("| |                                                 | |")
        print("| |                                                 | |")
        print("| |                     LOGIN                       | |")
        print("| |                                                 | |")
        print("| |                                                 | |")
        print("| |                                                 | |")
        print("| |_________________________________________________| |")
        print("|_____________________________________________________|")
        print("")
        print("")
        print("    PLEASE LOGIN WITH YOUR USERNAME AND PASSWORD: ")

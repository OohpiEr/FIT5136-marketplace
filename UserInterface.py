class UserInterface:
    def __init__(self):
        self.admin_menu_banner = """
          _||____________________________________________||_
        (__  ____________________________________________  __)
           ||                                            ||
           ||              -- MONASH SHOP --             ||
           ||                                            ||
           ||                   [ADMIN]                  ||
           ||                                            ||
           ||                                            ||
           ||                                            ||
          _||____________________________________________||_
        (__  ____________________________________________  __)
           ||                                            ||"""
        
        
        
    def display_admin_menu(self):
        print("  _||____________________________________________||_")
        print("(__  ____________________________________________  __)")
        print("   ||                                            ||")
        print("   ||              -- MONASH SHOP --             ||")
        print("   ||                                            ||")
        print("   ||                   [ADMIN]                  ||")
        print("   ||                                            ||")
        print("   ||                                            ||")
        print("   ||                                            ||")
        print("  _||____________________________________________||_")
        print("(__  ____________________________________________  __)")
        print("   ||                                            ||")
        print("")
        print("")
        print("     PLEASE SELECT AN OPTION")
        print("       [1] Add Item")
        print("       [2] Delete Item")
        print("       [3] Edit Item")
        print("       [Q] Back")
        print("")

    def display_customer_menu(self):
        print("  _||____________________________________________||_")
        print("(__  ____________________________________________  __)")
        print("   ||                                            ||")
        print("   ||              -- MONASH SHOP --             ||")
        print("   ||                                            ||")
        print("   ||                 [CUSTOMER]                 ||")
        print("   ||                                            ||")
        print("   ||                                            ||")
        print("   ||                                            ||")
        print("  _||____________________________________________||_")
        print("(__  ____________________________________________  __)")
        print("   ||                                            ||")
        print("")
        print("")
        print("     PLEASE SELECT AN OPTION")
        print("       [1] Browse All Items")
        print("       [2] View Shopping Cart")
        print("       [Q] Back")
        print("")

    def display_landing_page(self):
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
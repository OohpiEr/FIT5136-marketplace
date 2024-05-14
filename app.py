from Login import Login
from DbHelper import DbHelper
# from domain import Admin
# from domain import Customer
from UserInterface import UserInterface
from AdminInterface import AdminInterface
from controller import Controller
from controller import AdminController


class App:
    db = DbHelper()
    # ui = UserInterface()
    controller = Controller.Controller()
    EXIT_CODE = -1
    
    def __init__(self):
        self.login = Login()
        self.user = None

    def start(self):
        # self.login.login_control()
        curr_input = None
        while curr_input is not self.EXIT_CODE:
            # self.ui = AdminInterface()
            self.controller = AdminController()
            # self.controller.handle_input(inp)
            self.controller.home_page()
            
            # self.ui.display()
            # inp = input("Input: ")
            # print(inp)
            
        exit()
        self.login.login_control()
        self.ui.display_admin_menu()


if __name__ == "__main__":
    app = App()
    app.start()
    # a = Admin.Admin()
    # a.add_product("Colgate Total Charcoal Deep Clean Toothpaste",
    #     "Colgate",
    #     "Colgate Total Antibacterial Fluoride toothpaste has a unique formula that keeps your whole mouth healthy by fighting bacteria on teeth, tongue, cheeks, and gums for 12 hours*. Colgate Total Charcoal Deep Clean, active cleaning formula fights plaque even between teeth and hard to reach spaces",
    #     10,
    #     6.9,
    #     5,
        # 11)

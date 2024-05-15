from Login import Login
# from DbHelper import DbHelper
# from domain import Admin
# from domain.Customer import Customer
from domain.Inventory import Inventory
# from UserInterface import UserInterface
# from AdminInterface import AdminInterface
from Controller import Controller
# from controller import AdminController


class App:
    # db = DbHelper()
    # ui = UserInterface()
    inventory = Inventory()
    EXIT_CODE = -1

    def __init__(self):
        self.login = Login()
        # self.user = None

    def start(self):
        self.login.login_control(self.inventory)


if __name__ == "__main__":
    app = App()
    app.start()
from Login import Login
from domain.Inventory import Inventory
from Controller import Controller


class App:
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
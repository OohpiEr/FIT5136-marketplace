from Login import Login
from domain.Inventory import Inventory


class App:
    inventory = Inventory()
    EXIT_CODE = -1

    def __init__(self):
        self.login = Login()

    def start(self):
        self.login.login_control(self.inventory)


if __name__ == "__main__":
    app = App()
    app.start()
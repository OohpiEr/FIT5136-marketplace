from LoginController import LoginController
from domain.Inventory import Inventory
from DbHelper import DbHelper as db


class App:
    """Application class."""
    EXIT_CODE = -1

    def __init__(self):
        self.inventory = Inventory()
        self.__users = db.get_all_users(self.inventory)
        self.login = LoginController()

    def start(self):
        """Start the application."""
        self.login.login_control(self.__users)


if __name__ == "__main__":
    """Main entry point of the application."""
    app = App()
    app.start()
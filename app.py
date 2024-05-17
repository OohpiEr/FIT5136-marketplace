from Login import Login
from domain.Inventory import Inventory


class App:
    """Application class."""
    inventory = Inventory()
    EXIT_CODE = -1

    def __init__(self):
        self.login = Login()

    def start(self):
        """Start the application."""
        self.login.login_control(self.inventory)


if __name__ == "__main__":
    """Main entry point of the application."""
    app = App()
    app.start()
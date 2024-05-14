from AdminInterface import AdminInterface

class AdminController(Controller):
    def __init__(self):
        super().__init__()
        self.ui = AdminInterface()
        
    # def handle_input(self, input):
        
    def home_page(self):
        self.ui.display_home()
        inp = input("Input: ")
        print(inp)
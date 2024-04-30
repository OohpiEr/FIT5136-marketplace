from Login import Login


class App:
    def __init__(self):
        self.login = Login()
    
    def start(self):        
        self.login.login_control()
    
if __name__ == "__main__":
    app = App()
    app.start()
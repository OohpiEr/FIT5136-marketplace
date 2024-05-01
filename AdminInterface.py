from UserInterface import UserInterface

class AdminInterface(UserInterface):
    ADMIN_HOME_BANNER = """
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

    ADMIN_HOME_OPTIONS = [(1,"Add Item"), (2, "Delete Item"), (3, "Edit Item"), ("Q", "Back")]
    
    def __init__(self) -> None:
        super().__init__()
    
    def __display(self, banner, options, option_prompt):
        print(banner, "\n\n", option_prompt)
        for option in options:
            print(f"{self.TAB}[{option[0]}] {option[1]}")
        print(f"\n\n")
 
    def display(self):
        self.__display(self.ADMIN_HOME_BANNER, self.ADMIN_HOME_OPTIONS, self.OPTION_PROMPT)
        
        # print(self.admin_menu_banner,"\n\n",self.OPTION_PROMPT)
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

    ADMIN_HOME_OPTIONS = [(1,"Add Item"), (2, "Delete Item"), (3, "Edit Item"), ("Q", "Quit")]
    
    def __init__(self) -> None:
        super().__init__()
    
    def __display(self, banner, options, option_prompt):
        print(banner, "\n\n", option_prompt)
        for option in options:
            print(f"{self.TAB}[{option[0]}] {option[1]}")
        print(f"\n\n")
 
    # def display_home(self):
    #     self.__display(self.ADMIN_HOME_BANNER, self.ADMIN_HOME_OPTIONS, self.OPTION_PROMPT)
    #     return self.ADMIN_HOME_OPTIONS
        
    def display_home(self):
        options = ["1", "2", "3", "q"]
        
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
        print("       [1] Browse products (delete items)")
        print("       [2] Add product/categories")
        print("       [3] Update product")
        print("       [q] Quit")
        print("")

        return options
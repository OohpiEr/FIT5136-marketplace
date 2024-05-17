from UserInterface import UserInterface


class AdminInterface(UserInterface):
    """ User interface for admin"""
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

    ADMIN_HOME_OPTIONS = [("1", "Add Item"), ("2", "Delete Item"),
                          ("3", "Edit Item"), ("4", "Browse Item"), ("q", "Quit")]

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()

    def __display(self, banner, options, option_prompt):
        """Private method to display default banner, options and option prompt style display

        :param banner: banner string
        :param options: list of tuple containing options to display in the form of (option, option description) 
        :param option_prompt: prompt string to ask for option selection
        """
        print(banner, "\n\n", option_prompt)
        for option in options:
            print(f"{self.TAB}[{option[0]}] {option[1]}")
        print(f"\n\n")
        print(self.INPUT_PROMPT)

    def display_home(self):
        """display the home screen

        :return: list of tuple containing options displayed in the form of (option, option description)
        """
        self.__display(self.ADMIN_HOME_BANNER,
                       self.ADMIN_HOME_OPTIONS, self.OPTION_PROMPT)
        return self.ADMIN_HOME_OPTIONS

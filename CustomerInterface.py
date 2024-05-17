from UserInterface import UserInterface


class CustomerInterface(UserInterface):
    """Customer interface class. Display for customer interface."""
    CUST_HOME_BANNER = """
  _||____________________________________________||_
(__  ____________________________________________  __)
   ||                                            ||
   ||              -- MONASH SHOP --             ||
   ||                                            ||
   ||                 [CUSTOMER]                 ||
   ||                                            ||
   ||                                            ||
   ||                                            ||
  _||____________________________________________||_
(__  ____________________________________________  __)
   ||                                            ||"""

    CUST_PRODUCT_LIST_BANNER = """
  _||____________________________________________||_
(__  ____________________________________________  __)
   ||                                            ||
   ||              -- MONASH SHOP --             ||
   ||                                            ||
   ||                 [PRODUCTS]                 ||
   ||                                            ||
   ||                                            ||
   ||                                            ||
  _||____________________________________________||_
(__  ____________________________________________  __)
   ||                                            ||"""

    CUST_PRODUCT_LIST_BANNER = """
  _||____________________________________________||_
(__  ____________________________________________  __)
   ||                                            ||
   ||              -- MONASH SHOP --             ||
   ||                                            ||
   ||                    [ITEM]                  ||
   ||                                            ||
   ||                                            ||
   ||                                            ||
  _||____________________________________________||_
(__  ____________________________________________  __)
   ||                                            ||"""

    CUST_HOME_OPTIONS = [("1", "Browse All Products"),
                         ("2", "View Shopping Cart"), ("q", "Quit")]
    CUST_PRODUCT_OPTIONS = [("1", "Add to cart"),
                            ("2", "View Shopping Cart"), ("q", "Quit")]

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()

    def __display(self, banner, options, option_prompt):
        """Private method to display default banner, options and option prompt style display

        :param banner: banner string
        :param options: list of tuple containing options to display in the form of (option, option description) 
        :param option_prompt: prompt string to ask for option selection
        """
        print(banner, self.NEWLINE, self.NEWLINE, option_prompt)
        for option in options:
            print(f"{self.TAB}[{option[0]}] {option[1]}")
        print(self.NEWLINE, self.NEWLINE)
        print(self.INPUT_PROMPT)

    def display_home(self):
        """Displays the home page for the customer

        :return: list of tuple containing options displayed in the form of (option, option description)
        """
        self.__display(self.CUST_HOME_BANNER,
                       self.CUST_HOME_OPTIONS, self.OPTION_PROMPT)
        return self.CUST_HOME_OPTIONS

    def display_product_list(self, product_list):
        """Display the product list for the product list screen

        :param product_list: list of product objects
        :return: list of tuple containing options displayed in the form of (option, option description)
        """
        display_options = []
        options = []

        for i, product in enumerate(product_list):
            display_options.append(
                (i+1, f"{product.name} | ${product.og_price}"))
            options.append((i, product))

        display_options.append(self.QUIT_OPTION)

        self.__display(self.CUST_PRODUCT_LIST_BANNER,
                       display_options, self.OPTION_PROMPT)

        return options

    def display_product_details(self, product):
        """Displays the product details screen

        :param product: product object to display
        :return: list of tuple containing options displayed in the form of (option, option description)
        """
        print(self.CUST_PRODUCT_LIST_BANNER)
        print(self.TAB, f"NAME: {product.name}")
        print(self.TAB, f"BRAND: {product.brand}")
        print(self.TAB, f"QUANTITY: {product.quantity}")

        print(self.NEWLINE, self.TAB, f"PRICE: ${product.og_price}")
        print(self.TAB, f"MEMBER PRICE: ${product.member_price}")

        print(self.NEWLINE, self.TAB, "DESCRIPTION:",
              self.NEWLINE, self.TAB,  self.TAB, product.description)

        print(self.NEWLINE, self.TAB,  f"CATEGORY: {product.category.name}")
        print(self.TAB, f"SUB-CATEGORY: {product.sub_category.name}")
        print(self.NEWLINE, self.NEWLINE, self.OPTION_PROMPT)

        for option in self.CUST_PRODUCT_OPTIONS:
            print(f"{self.TAB}[{option[0]}] {option[1]}")

        print(self.NEWLINE, self.NEWLINE, self.INPUT_PROMPT)

        return self.CUST_PRODUCT_OPTIONS

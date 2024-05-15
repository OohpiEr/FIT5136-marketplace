from UserInterface import UserInterface


class CustomerInterface(UserInterface):
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

    CUST_HOME_OPTIONS = [("1", "Browse All Products"),
                         ("2", "View Shopping Cart"), ("q", "Quit")]
    CUST_PRODUCT_OPTIONS = [("1", "Add to cart"),
                         ("2", "View Shopping Cart"), ("q", "Quit")]

    def __init__(self) -> None:
        super().__init__()

    def __display(self, banner, options, option_prompt):
        print(banner, "\n\n", option_prompt)
        for option in options:
            print(f"{self.TAB}[{option[0]}] {option[1]}")
        print(f"\n\n")
        print(self.INPUT_PROMPT)

    def display_home(self):
        self.__display(self.CUST_HOME_BANNER,
                       self.CUST_HOME_OPTIONS, self.OPTION_PROMPT)
        return self.CUST_HOME_OPTIONS

    def display_product_list(self, product_list):
        options = []
        for i, product in enumerate(product_list):
            options.append((i+1, f"{product.name} | ${product.og_price}"))
        self.__display(self.CUST_PRODUCT_LIST_BANNER,
                       options, self.OPTION_PROMPT)

    def display_product_details(self, product):
        print(f"NAME: {product.name}")
        print(f"BRAND: {product.brand}")
        print(f"QUANTITY: {product.quantity}")

        print(self.NEWLINE, f"PRICE: ${product.og_price}")
        print(f"MEMBER PRICE: ${product.member_price}")

        print(self.NEWLINE, "DESCRIPTION:", self.NEWLINE, product.description)
        
        print(self.NEWLINE, f"CATEGORY: ${product.category}")
        print(f"SUB-CATEGORY: ${product.sub_category}")
        
        for option in self.CUST_PRODUCT_OPTIONS:
            print(f"{self.TAB}[{option[0]}] {option[1]}")




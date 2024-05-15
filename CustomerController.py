from UserInputError import UserInputError
from CustomerInterface import CustomerInterface
from RowNotFoundError import RowNotFoundError
from domain.Customer import Customer


class CustomerController():
    def __init__(self):
        # super().__init__()
        self.ui = CustomerInterface()
        self.customer = Customer()

    def home_page(self):
        self.ui.display_home()
        inp = input("Input: ")
        print(inp)

    def customer_control(self):
        quit_flag = False
        display_menu = True
        while not quit_flag:
            if display_menu:
                self.ui.display_home()

            inp = input().strip().lower()

            try:
                if len(inp) == 0:
                    raise UserInputError

                match inp:
                    case "1":
                        self.browse_all_products()
                        display_menu = True
                    case "2":
                        self.view_shopping_cart()
                        display_menu = True
                    case "q":
                        return
                    case _:
                        display_menu = False
                        raise UserInputError
            except UserInputError as e:
                print(
                    "Invalid input. Please enter 1, 2 to perform an action or 'q' to quit.")
        

    def view_shopping_cart(self):
        # TODO: implement shopping cart
        pass

        

    def browse_all_products(self):
        quit_flag = False
        display_menu = True

        while not quit_flag:
            if display_menu:
                products = self.customer.get_all_products()
                self.ui.display_product_list(products)

            inp = input().strip().lower()

            # TODO: implement
            # try:
            #     if len(inp) == 0:
            #         raise UserInputError

            #     match inp:
            #         case "1":
            #             self.browse_all_products()
            #             display_menu = True
            #         case "2":
            #             self.view_shopping_cart()
            #             display_menu = True
            #         case "q":
            #             return
            #         case _:
            #             display_menu = False
            #             raise UserInputError
            # except UserInputError as e:
            #     print(
            #         "Invalid input. Please enter 1, 2 to perform an action or 'q' to quit.")
        

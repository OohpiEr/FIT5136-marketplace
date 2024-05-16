

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_to_cart(self, product):
        try:
            num_add = int(input(f"How many '{product.name}' do you want to add to the shopping cart? "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        # Check if the product is available in inventory
        if int(product.quantity) < num_add:
            print(f"Sorry, only {product.quantity} '{product.name}' available.")
            return

            # Check if the product is already in the cart
        for item in self.items:
            if item["product"].id == product.id:
                item["quantity"] += num_add
                print(f"{num_add} '{product.name}' added to the shopping cart.")
                return

        # If the product is not in the cart, add it
        self.items.append({"product": product, "quantity": num_add})
        print(f"{num_add} '{product.name}' added to the shopping cart.")

    def view_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart Contents:")
            print(f"{'Name':<50} {'Quantity':<10} {'Price':<10}")
            total_price = 0
            for item in self.items:
                product = item["product"]
                quantity = item["quantity"]
                price =  float(product.og_price)
                total_price += price * quantity
                print(f"{product.name:<50} {quantity:<10} ${price:.2f}")
            print(f"{'Total Price:':<50} ${total_price:.2f}")
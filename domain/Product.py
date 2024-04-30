class Product:
    def __init__(self, product_id, name, brand, description, quantity, category, subscription, og_price, member_price):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.description = description
        self.quantity = quantity
        self.category = category
        self.subscription = subscription
        self.og_price = og_price
        self.member_price = member_price

    def __str__(self):
        return "product_id = {}\nname = {}\nbrand = {}\ndescription = {}\nquantity = {}\ncategory = {}\nsubscription = {}\nog_price = {}\nmember_price = {}".format(
            self.product_id,
            self.name,
            self.brand,
            self.description,
            self.quantity,
            self.category,
            self.subscription,
            self.og_price,
            self.member_price)

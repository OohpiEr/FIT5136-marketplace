from domain.Product import Product
import csv

class Customer:
    def __init__(self):
        return

    def add_product_to_cart(self):
        cart_add = input("Add to Cart (please enter the name of the product you wish to add to cart): ")
        with open('db/product.txt', 'r+', newline='') as f2:
            with open('db/cart.txt', 'w', newline='') as w2:
                reader = csv.reader(f2, delimiter=',')
                ####writer = csv.writer(w2)
                int_list = []
                #for str in reader:
                #   int_list.append(int(x) for x in str[4])
                #for index, row in enumerate(reader):
                for row in reader:
                    if cart_add in row[1]:  # and int_list[index] >= 1:
                        for index, line in enumerate(reader):
                            if cart_add in row[1]:
                                #qty = int(row[index][4])
                                qty = int(row[4])
                                if qty >= 1:
                                    print(qty)
                                    w2.write(cart_add + '\n')
                                    print("You have successfully added ", cart_add)
                                    #writer.writerow(cart_add + '\n')
                    else:
                        print("That item is not in stock or is not selling")
                #print("You have successfully added ", cart_add)


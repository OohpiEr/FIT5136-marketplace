# from DbHelper import DbHelper as db

# from domain.Product import Product
import csv

class Customer:
    def __init__(self,inventory):
        self.inventory = inventory

    def get_all_products(self):
        return self.inventory.products

    #def add_product_to_cart(self):
     #   cart_add = input("Add to Cart (please enter the product ID number of the product you wish to add to cart): ")
      #  with open('db/product.txt', 'r+', newline='') as f2:
       #     with open('db/cart.txt', 'a', newline='') as w2:
        #        reader = csv.reader(f2, delimiter=',')
         #       for row in reader:
          #          if row and row[0] == cart_add:  # Code inspired from Author: wwii, Link: https://stackoverflow.com/questions/39336449/python-check-if-value-in-csv-file
           #             w2.write(str(row))
            #            w2.write('\n')
             #           print("You have successfully added ", row)
              #      else:
               #         print("That item is not in stock or is not selling")


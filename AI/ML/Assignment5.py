# class Products :
#     count = 0

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         Products.count+=1

#     def get_product(self):
#         print(f"The price of {self.name} is Rs. {self.price}")

#     @classmethod
#     def get_count(cls):
#         print(f"The total count is {cls.count}")

#     @staticmethod
#     def product_discount(price,discount):
#         product_price = price-(price*(discount/100))
#         print(f"Discount offered is {discount}% and the final price is Rs. ",product_price)

# p1 = Products("laptop",90_000)
# p2 = Products("iphone",100_000)

# p1.get_product()
# p2.get_product()

# Products.get_count()

# Products.product_discount(90000,8)

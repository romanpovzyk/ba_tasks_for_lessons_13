# class Product:
#     def __init__(self, type, name, price):
#         self.type = type
#         self.name = name
#         self.price = price
#
# class ProductStore(Product):
#     def __init__(self):
#         super().__init__(type, name, price)
#
#     def add(self, product, amount):
#         self.product = product
#         self.amount = amount
#
#
#
# p = Product('Sport', 'Football T-Shirt', 100)
# p2 = Product("Food", "Ramen", 1.5)
# s = ProductStore()
# print(s.add(p, 10))
# print(p)
# s.add(p2, 300)
# #s.sell(‘Ramen’, 10)
# #assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

class Product():
    def __init__(self,id,product,price,catogery):
        self.id = id 
        self.product = product
        self.price = price
        self.catogery = catogery

    def __str__(self):
        return f"\n id : {self.id} \n product : {self.product} \n price : {self.price} \n catogery : {self.catogery} \n"
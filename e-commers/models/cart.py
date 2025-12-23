class Cart():
    def __init__(self) :
        self.cart = []

    def addCart(self,product):
        if product not in self.cart :
            self.cart.append(product)
            print("the product is added..")
        else :
            print("the proudect already in the cart.")

    def removeCart(self,product):
        if product in self.cart:
            self.cart.remove(product)
            print("the product is removed..")
        else :
            print("the product is not in the cart.")
                
    def showCart(self):
        if  not self.cart :
            print("the cart is empty.")
        else :
            for p in self.cart:
                print(p)

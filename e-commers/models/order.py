from datetime import datetime 

class OrderItem:
    def __init__(self,quantity,product):
        self.product = product
        self.quantity = quantity

    def totalPrice(self):
        return self.product.price * self.quantity 

    def __str__(self):
        return f"product : {self.product.name} \n price : {self.product.price} \n quantity  : {self.quantity}\n"


class Order :
    def __init__(self, id ,items , user_id, status= "pending" ) :
        self.id      = id 
        self.items = items
        self.user_id = user_id
        self.status  = status 
        self.time    = datetime.now()
        self.total_price = self.calculateTotal()
    
    def __str__(self): 
        items_str = "\n".join(str(item) for item in self.items)
        return f"\n summary order :\n clinet id : {self.id} \n items is : \n {items_str} \n total price : {self.total_price} \n the time : {self.time} \n status : {self.status}"

    def calculateTotal(self):
        total = 0 
        for item in self.items :
            total += item.totalPrice()
        return total



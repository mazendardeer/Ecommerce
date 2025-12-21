from cart import Cart 
from products import Product
from users import User
from order import Order , OrderItem

cart = Cart(1)
P1 = Product(1,"laptop",200,"computer",20)
P2 = Product(2,"iphon",300,"mobil",30)

I1 = OrderItem(50, P1)
I2 = OrderItem(10,P2)

cart.addCart(P1,20)
cart.showCart()



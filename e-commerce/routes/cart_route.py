from flask import render_template , Blueprint , request , redirect , url_for
from models import Cart

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/", methods=["GET" , "POST"]) 
def add_cart(): 
    product_id = request.form.get("product_id") 
    quantity   = request.form.get("quantity") 
    Cart.cartAdd(product_id,quantity) 
    return render_template("home_page.html")

@cart_bp.route("/cart") 
def show_cart(): 
    user_id = 1 
    cart = Cart.view_cart(user_id)
    return render_template("cart.html",cart = cart)
    



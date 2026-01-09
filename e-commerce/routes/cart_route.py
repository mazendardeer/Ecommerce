from flask import Blueprint, request, redirect, url_for, render_template, session
from models import Cart
import uuid

cart_bp = Blueprint("cart_bp", __name__)

def get_guest_id():
    if "guest_id" not in session:
        session["guest_id"] = str(uuid.uuid4())
    return session["guest_id"]

@cart_bp.route("/", methods=["POST"])
def add_cart():
    product_id = request.form.get("product_id")
    quantity   = int(request.form.get("quantity", 1))

    guest_id = get_guest_id()
    cart = Cart(guest_id)
    cart.cartAdd(product_id, quantity)
    return redirect(url_for("main_bp.view_products"))

@cart_bp.route("/cart")
def show_cart():
    guest_id = get_guest_id()
    cart_items = Cart.view_cart(guest_id)
    return render_template("cart.html", cart=cart_items)

@cart_bp.route("/remove", methods= ["POST"])
def remove_cart():
    guest_id = get_guest_id()
    product_id = request.form.get("product_id")
    cart = Cart(guest_id)
    cart.delet_cart(product_id,guest_id)
    return redirect(url_for("cart_bp.show_cart"))


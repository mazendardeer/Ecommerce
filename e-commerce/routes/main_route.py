from flask import Blueprint , render_template
from models import Product

main = Blueprint("main",__name__)

@main.route("/")
def view_products():
    products  = Product.get_product()
    return render_template("home_page.html",products=products)
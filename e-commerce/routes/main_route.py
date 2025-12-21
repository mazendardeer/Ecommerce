from flask import Blueprint , render_template
from models import Product

main_bp = Blueprint("main_bp",__name__)

@main_bp.route("/")
def view_products():
    products  = Product.get_product()
    return render_template("home_page.html",products=products)
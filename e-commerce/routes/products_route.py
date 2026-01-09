from flask import Blueprint , render_template
from models import Product

products_bp = Blueprint("products_bp",__name__)

@products_bp.route("/products")
def view_products():
    products  = Product.get_product()
    return render_template("products.html",products=products)
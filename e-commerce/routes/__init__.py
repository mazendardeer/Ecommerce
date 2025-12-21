from flask import Blueprint
from .auth_route import *
from .cart_route import *
from .homePage_route import *


auth = Blueprint("auth", __name__)
cart = Blueprint("cart", __name__)
ecommerce = Blueprint("homePage",__name__)






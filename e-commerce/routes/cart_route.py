from routes import cart 
from flask import flash , request , redirect , render_template

@cart.route("/")
def cartPage():
    pass
from routes import ecommerce 
from flask import flash , request , redirect , render_template

@ecommerce.route("/")
def homePage():
    return render_template("home_page.html")
from flask import Flask 
from routes.auth_route import auth 
from routes.cart_route import cart_bp
from routes.main_route import main


app = Flask(__name__)
app.register_blueprint(auth ,url_prefix="/auth")
app.register_blueprint(cart_bp ,url_prefix="/cart")
app.register_blueprint(main)


if __name__ == "__main__":
    app.run(debug=True, port=9000)

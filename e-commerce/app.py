from flask import Flask 
from routes import auth_bp
from routes import cart_bp
from routes import main_bp


app = Flask(__name__)
app.register_blueprint(auth_bp ,url_prefix="/auth")
app.register_blueprint(cart_bp ,url_prefix="/cart")
app.register_blueprint(main_bp,)


if __name__ == "__main__":
    app.run(debug=True, port=9000)

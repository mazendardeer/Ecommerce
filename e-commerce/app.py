from flask import Flask
from routes import auth_bp
from routes import cart_bp
from routes import main_bp

from db import getConnection


app = Flask(__name__)
app.secret_key = "secret_key_123"

app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(main_bp)


if __name__ == "__main__":
    app.run(debug=True, port=9000)

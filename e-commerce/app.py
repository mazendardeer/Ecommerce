from flask import Flask, render_template
from models import *
from routes import *


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=9000)

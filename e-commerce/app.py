from flask import Flask, render_template
from models.cart import Cart
from models.users import User, usersTable, usersInsertion

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("home_page.html")

# 1️⃣ إنشاء جدول المستخدمين
usersTable()

# 2️⃣ إضافة المستخدم
user = User(id=None, name="Mazen", email="mazen@example.com", password="123456")
user_id = usersInsertion(user)  # ترجع ID الفعلي

# 3️⃣ إنشاء كارت للمستخدم
cart = Cart(user_id=user_id)
cart.createTable()
cart.createCard_item()

# 4️⃣ إضافة 10 منتجات مختلفة
cart.cartAdd(product_id=1, quantity=2)
cart.cartAdd(product_id=2, quantity=1)
cart.cartAdd(product_id=3, quantity=5)
cart.cartAdd(product_id=4, quantity=3)
cart.cartAdd(product_id=5, quantity=2)
cart.cartAdd(product_id=6, quantity=4)
cart.cartAdd(product_id=7, quantity=1)
cart.cartAdd(product_id=8, quantity=6)
cart.cartAdd(product_id=9, quantity=2)
cart.cartAdd(product_id=10, quantity=3)

if __name__ == "__main__":
    app.run(debug=True, port=9000)

from db import getConnection

class Cart:
    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def createTable():
        db = getConnection()
        cursor = db.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cart (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL UNIQUE,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                ) ENGINE=InnoDB
            """)
            print("Cart table created.")
        except Exception as Error:
            print(f"Error creating cart table: {Error}")
        finally:
            db.commit()
            cursor.close()
            db.close()
    @staticmethod
    def createCart_Item():
        db = getConnection()
        cursor = db.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cart_item(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cart_id INT NOT NULL,
                    product_id INT NOT NULL,
                    quantity INT NOT NULL,
                    FOREIGN KEY(cart_id) REFERENCES cart(id),
                    FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
                ) ENGINE=InnoDB
            """)
            print("Cart_item table created.")
        except Exception as Error:
            print(f"Error creating cart_item table: {Error}")
        finally:
            db.commit()
            cursor.close()
            db.close()
    
    def cartAdd(self, product_id, quantity=1):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        Cart.createTable()
        Cart.createCart_Item()
        
        try:
            # تأكد من وجود المنتج
            cursor.execute("SELECT id FROM products WHERE id=%s", (product_id,))
            if cursor.fetchone() is None:
                print(f"Product id={product_id} does not exist!")
                return

            # الحصول على cart للمستخدم
            cursor.execute("SELECT id FROM cart WHERE user_id=%s", (self.user_id,))
            cart = cursor.fetchone()
            if cart is None:
                cursor.execute("INSERT INTO cart (user_id) VALUES(%s)", (self.user_id,))
                cart_id = cursor.lastrowid
            else:
                cart_id = cart[0]

            # تحقق من وجود المنتج في الكارت
            cursor.execute(
                "SELECT id, quantity FROM cart_item WHERE cart_id=%s AND product_id=%s",
                (cart_id, product_id)
            )
            cart_item = cursor.fetchone()
            if cart_item is None:
                cursor.execute(
                    "INSERT INTO cart_item (cart_id, product_id, quantity) VALUES (%s, %s, %s)",
                    (cart_id, product_id, quantity)
                )
            else:
                new_quantity = cart_item[1] + quantity
                cursor.execute(
                    "UPDATE cart_item SET quantity=%s WHERE id=%s",
                    (new_quantity, cart_item[0])
                )
            print(f"Product id={product_id} added/updated in cart.")

        except Exception as Error:
            print(f"Error in cart insertion: {Error}")

        finally:
            db.commit()
            cursor.close()
            db.close()

    def cartRemove(self, cart_id, product_id):
        db = getConnection()
        cursor = db.cursor(buffered=True)
        try:
            cursor.execute(
                "SELECT id FROM cart_item WHERE cart_id=%s AND product_id=%s",
                (cart_id, product_id)
            )
            item = cursor.fetchone()
            if item:
                cursor.execute(
                    "DELETE FROM cart_item WHERE cart_id=%s AND product_id=%s",
                    (cart_id, product_id)
                )
                print(f"Product id={product_id} removed from cart.")
            else:
                print("Product not in the cart.")
        except Exception as Error:
            print(f"Error removing cart item: {Error}")
        finally:
            db.commit()
            cursor.close()
            db.close()
    @staticmethod
    def view_cart(user_id):
        db = getConnection()
        cursor = db.cursor(dictionary=True)
        try :
            cursor.execute("SELECT * FROM cart WHERE user_id=%s" , (user_id,))
            result = cursor.fetchall()
            if not result:
                return []
            return result
    
        except Exception as Error :
            print(f"wrong in cart..{Error}")

        finally:
            cursor.close()
            db.close()

